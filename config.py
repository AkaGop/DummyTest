# config.py
CEID_MAP = {
    11: "Equipment Offline", 12: "Control State Local", 13: "Control State Remote", 101: "Alarm Cleared", 102: "Alarm Set", 120: "IDRead", 127: "LoadedToTool", 131: "LoadToToolCompleted", 132: "UnloadFromToolCompleted", 136: "MappingCompleted", 141: "PortStatusChange", 151: "MagazineDocked", 181: "MagazineDocked", 182: "MagazineUndocked",
}
RPTID_MAP = {
    151: ['Timestamp', 'PortID', 'MagazineID', 'OperatorID'],
    141: ['Timestamp', 'PortID', 'PortStatus'],
    120: ['Timestamp', 'LotID', 'PanelID'],
    101: ['Timestamp', 'AlarmIDValue'],
}
CRITICAL_ALARM_IDS = [1, 2, 190, 191, 1050, 1051, 1052, 4336, 4337]
ALARM_MAP = {1: "CPU error", 2: "SafetyPLC error", 113: "HNC error", 190: "Emergency stop"}
