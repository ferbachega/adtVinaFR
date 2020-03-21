from adtFRconfig import *
from ConvertPDBFilesToPDBQT import prepare_ligands_from_PDB_folder


LIGANDSOURCE = 'examples/ligands_PDB'
LIGAND_PDBQT = 'examples/ligands_PDBQT'

prepare_ligands_from_PDB_folder(LIGANDSOURCE , LIGAND_PDBQT)
