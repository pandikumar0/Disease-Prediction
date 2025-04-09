ORDERED_FEATURES = [
    "FP1", "FP2", "F3", "F4", "C3", "C4", "P3", "P4", "O1", "O2", "F7", "F8", "P7", "P8", "Fz", "Cz", "Pz",
    "FC1", "FC2", "CP1", "CP2", "FC5", "FC6", "CP5", "CP6", "EMG1", "EMG2", "IO", "EMG3", "EMG4",
    "LShankACCX", "LShankACCY", "LShankACCZ", "LShankGYROX", "LShankGYROY", "LShankGYROZ",
    "RShankACCX", "RShankACCY", "RShankACCZ", "RShankGYROX", "RShankGYROY", "RShankGYROZ",
    "WaistACCX", "WaistACCY", "WaistACCZ", "WaistGYROX", "WaistGYROY", "WaistGYROZ",
    "ArmACCX", "ArmACCY", "ArmACCZ", "ArmGYROX", "ArmGYROY", "ArmGYROZ"
]

DEFAULT_VALUES = [
    23.8237, 25.2929, 24.5446, 28.625, 24.6709, 17.8673, 22.8003, 16.2957, 24.5238, 3.7206, 20.9063, 22.6086,
    26.402, 27.4016, 22.5426, 39.1442, 21.1925, 26.9104, 44.5521, 20.9134, 20.4606, 20.0418, 20.9046, 21.2456,
    24.9607, 3242, 2742.5, -23, -4198, 3557, 7763.86147, -772.18443, -3471.14131, -109.94899, -14.1734,
    -3.79334, 7763.86147, -772.18443, -3471.14131, -109.94899, -14.1734, -3.79334, -661.66428, 5360.04006,
    5945.97726, 55.29625, 48.01602, 8.69861, -661.66428, 5360.04006, 5945.97726, 55.29625, 48.01602, 8.69861
]

FEATURE_GROUPS = {
    "EEG - Frontal": ["FP1", "FP2", "F3", "F4", "F7", "F8", "Fz"],
    "EEG - Central": ["C3", "C4", "Cz"],
    "EEG - Parietal": ["P3", "P4", "P7", "P8", "Pz"],
    "EEG - Occipital": ["O1", "O2"],
    "EEG - FC & CP": ["FC1", "FC2", "CP1", "CP2", "FC5", "FC6", "CP5", "CP6"],
    "EMG": ["EMG1", "EMG2", "EMG3", "EMG4"],
    "Other Sensor": ["IO"],
    "LShank Sensors": ["LShankACCX", "LShankACCY", "LShankACCZ", "LShankGYROX", "LShankGYROY", "LShankGYROZ"],
    "RShank Sensors": ["RShankACCX", "RShankACCY", "RShankACCZ", "RShankGYROX", "RShankGYROY", "RShankGYROZ"],
    "Waist Sensors": ["WaistACCX", "WaistACCY", "WaistACCZ", "WaistGYROX", "WaistGYROY", "WaistGYROZ"],
    "Arm Sensors": ["ArmACCX", "ArmACCY", "ArmACCZ", "ArmGYROX", "ArmGYROY", "ArmGYROZ"]
}

IMPORTANT_FEATURES = [
    "IO", "EMG1", "EMG4", "ArmGYROZ", "EMG3", "WaistGYROY", "EMG2",
    "LShankACCZ", "P7", "CP6", "O2", "WaistACCX", "P3", "WaistACCY",
    "CP2", "ArmACCX", "WaistGYROX", "LShankGYROZ", "FC1"
]