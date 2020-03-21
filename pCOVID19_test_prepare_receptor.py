from adtFRconfig import *
from adtVinaRFBabel.ConvertPDBFilesToPDBQT import prepare_flexible_receptor_from_PDB_folder


RECEPTORSOURCE = 'examples/pCOVID19/flexible_receptor_PDB'  
RECEPTOR_PDBQT = 'examples/pCOVID19/flexible_receptor_PDBQT'

prepare_flexible_receptor_from_PDB_folder(RECEPTORSOURCE , RECEPTOR_PDBQT)
