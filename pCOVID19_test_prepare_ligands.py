from adtFRconfig import *
from adtVinaRFBabel.ConvertPDBFilesToPDBQT import prepare_ligands_from_PDB_folder


LIGANDSOURCE = 'examples/pCOVID19/ligands_PDB'
LIGAND_PDBQT = 'examples/pCOVID19/ligands_PDBQT'

prepare_ligands_from_PDB_folder(LIGANDSOURCE , LIGAND_PDBQT)
