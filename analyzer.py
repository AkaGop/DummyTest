# analyzer.py
from datetime import datetime
import pandas as pd
from collections import Counter

def find_alarm_correlations(df: pd.DataFrame) -> dict:
    """
    Analyzes the log for patterns preceding alarms to aid in predictive maintenance.
    """
    # We only care about alarms that actually happened
    if 'details.AlarmID' not in df.columns or df['details.AlarmID'].notna().sum() == 0:
        return {}

    alarm_events = df[df['details.AlarmID'].notna()]
    precursor_patterns = []
    
    # Analyze the 3 events leading up to each alarm
    for idx in alarm_events.index:
        if idx > 2:
            # Get the 'EventName' of the three previous events
            sequence = tuple(df.loc[idx-3:idx-1, 'EventName'])
            alarm_id = alarm_events.loc[idx, 'details.AlarmID']
            precursor_patterns.append({'sequence': sequence, 'alarm_id': alarm_id})

    if not precursor_patterns:
        return {}
        
    # Count the occurrences of each unique (sequence -> alarm) pattern
    pattern_counts = Counter(
        f"{' -> '.join(p['sequence'])} leads to ALARM {p['alarm_id']}" for p in precursor_patterns
    )
    
    # Format the results for display
    correlation_df = pd.DataFrame(pattern_counts.items(), columns=['Pattern', 'Occurrences'])
    correlation_df.sort_values(by='Occurrences', ascending=False, inplace=True)
    
    return correlation_df

def perform_eda(df: pd.DataFrame) -> dict:
    """Performs Exploratory Data Analysis on the parsed log data."""
    eda_results = {}
    if 'EventName' in df.columns:
        eda_results['event_counts'] = df['EventName'].value_counts()
    else:
        eda_results['event_counts'] = pd.Series(dtype='int64')

    if 'details.AlarmID' in df.columns:
        alarm_events = df[df['details.AlarmID'].notna()].copy()
        if not alarm_events.empty:
            alarm_ids = pd.to_numeric(alarm_events['details.AlarmID'], errors='coerce').dropna()
            eda_results['alarm_counts'] = alarm_ids.value_counts()
            eda_results['alarm_table'] = alarm_events[['timestamp', 'EventName', 'details.AlarmID']]
            # --- NEW: Call the correlation analysis ---
            eda_results['alarm_correlations'] = find_alarm_correlations(df)
        else:
            eda_results['alarm_counts'] = pd.Series(dtype='int64')
            eda_results['alarm_table'] = pd.DataFrame()
            eda_results['alarm_correlations'] = pd.DataFrame()
    else:
        eda_results['alarm_counts'] = pd.Series(dtype='int64')
        eda_results['alarm_table'] = pd.DataFrame()
        eda_results['alarm_correlations'] = pd.DataFrame()
        
    return eda_results

# ... (The `analyze_data` function remains unchanged) ...
def analyze_data(events: list) -> dict:
    # This function is correct and does not need to be changed.
    # I have omitted it for brevity, but it should be present in your file.
    pass # Placeholder
