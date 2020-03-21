#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ConvertPDBFilesToPDBQT.py
#  
#  Copyright 2020 Fernando <fernando@winter>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
from adtFRconfig import *

def list_pdb_files(folder):
	""" Function doc """
	files   = os.listdir(folder)
	pdblist = []
	for _file in files:
		_file2 = _file.split('.')
		if _file2[1] == 'pdb':
			#print _file
			_file3 = os.path.join(folder, _file)
			pdblist.append(_file3)
	return pdblist
			

""" 

 - - - - - - R E C E P T O R - - - - - - 

"""		

def run_prepare_recpetor4 (receptor_filename, pdbqt_out):
	""" Function doc """
	cmd = os.path.join(AUTODOCKTOOLS, 'prepare_receptor4.py')	
	os.system(cmd + ' -r ' + receptor_filename + ' -o ' + pdbqt_out + ' -A checkhydrogens') #("parmchk -i " + AMBERTOOLS_outputs+"/"+new_ligand_name+".mol2 " + " -f mol2 -o "+AMBERTOOLS_outputs+"/"+new_ligand_name+".frcmod")




def prepare_flexible_receptor_from_PDB_folder(folderin , folderout):
	""" prepare flexible receptor (several pdbqt files) from pdb files """

	pdblist  = list_pdb_files(folderin)
	pdbqt_list = []
	


	#folderout = os.environ.get('PDYNAMO_SCRATCH') 
	if not os.path.isdir(folderout):              
		print folderout, "not found"              
		os.mkdir(folderout)                       
		print "creating: ", folderout             
                                                    
	
	
	
	
	for pdbfile in pdblist:
		
		pdbfile_splited = os.path.split(pdbfile)
		#print pdbfile_splited 

		_file = pdbfile_splited[-1]
		#print _file 

		outputname = _file[:-3] + 'pdbqt'	
		#print outputname 

		outputname = os.path.join(folderout, outputname)
		
		
		print '\n Generating receptor:', outputname 
		run_prepare_recpetor4 (pdbfile, outputname)
		pdbqt_list.append(outputname)
	
	return pdbqt_list



""" 

 - - - - - - L I G A N D S - - - - - - 

"""		

def run_prepare_ligand4 (ligand_filename, pdbqt_out):
	""" Function doc """
	cmd = os.path.join(AUTODOCKTOOLS, 'prepare_ligand4.py')	
	os.system(cmd + ' -l ' + ligand_filename + ' -o ' + pdbqt_out) #("parmchk -i " + AMBERTOOLS_outputs+"/"+new_ligand_name+".mol2 " + " -f mol2 -o "+AMBERTOOLS_outputs+"/"+new_ligand_name+".frcmod")



def prepare_ligands_from_PDB_folder(folderin = None , folderout = None):
	
	pdblist    = list_pdb_files(folderin)
	pdbqt_list = []
	
	
	if not os.path.isdir(folderout):              
		#print folderout, "not found"              
		try:
			print "Creating: ", folderout             
			os.mkdir(folderout)                       

		except:                               
			print 'Unable to create: ', folderout
	
	
	for pdbfile in pdblist:
		
		
		pdbfile_splited = os.path.split(pdbfile)
		#print pdbfile_splited 

		_file = pdbfile_splited[-1]
		#print _file 

		outputname = _file[:-3] + 'pdbqt'	
		#print outputname 

		outputname = os.path.join(folderout, outputname)
		
		
		#outputname = pdbfile[:-3] + 'pdbqt'
		run_prepare_ligand4 (pdbfile, outputname)
		pdbqt_list.append(outputname)

	return pdbqt_list




