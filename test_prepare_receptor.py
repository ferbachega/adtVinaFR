from adtFRconfig import *
from ConvertPDBFilesToPDBQT import prepare_flexible_receptor_from_PDB_folder


RECEPTORSOURCE = 'examples/flexible_receptor_PDB'
RECEPTOR_PDBQT = 'examples/flexible_receptor_PDBQT'

prepare_flexible_receptor_from_PDB_folder(RECEPTORSOURCE , RECEPTOR_PDBQT)
