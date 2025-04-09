from setuptools import setup

APP = ['papering_ui.py']  # Replace with your entry point
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['PyQt6'],
    'includes': [
        'PyQt6.QtWidgets',
        'PyQt6.QtGui',
        'PyQt6.QtCore',
        'papering_database',  # Add papering_database module
        'papering_def',        # Add papering_def module
    ],
    'resources': ['icons'],  # Add fonts/icons/etc here if needed
    'iconfile': 'icon.icns',  # Optional: your .icns app icon
}

setup(
    app=APP,
    name='Papering',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
