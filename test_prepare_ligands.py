from adtFRconfig import *
from ConvertPDBFilesToPDBQT import prepare_ligands_from_PDB_folder


LIGANDSOURCE = '/home/fernando/programs/adtVinaFR/ligands_PDB'
LIGAND_PDBQT = '/home/fernando/programs/adtVinaFR/ligands_PDBQT'

prepare_ligands_from_PDB_folder(LIGANDSOURCE , LIGAND_PDBQT)
