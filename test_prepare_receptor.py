from adtFRconfig import *
from ConvertPDBFilesToPDBQT import prepare_flexible_receptor_from_PDB_folder


RECEPTORSOURCE = '/home/fernando/programs/adtVinaFR/flexible_receptor_PDB'
RECEPTOR_PDBQT = '/home/fernando/programs/adtVinaFR/flexible_receptor_PDBQT'

prepare_flexible_receptor_from_PDB_folder(RECEPTORSOURCE , RECEPTOR_PDBQT)
