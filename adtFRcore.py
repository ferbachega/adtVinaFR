#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
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

def vina_logparser (logfile, ligand_name, receptor_name):
	""" Function doc """
	
	logfile = open(logfile, 'r')
	output_list = []
	
	for line in logfile:
		linesplit = line.split()
		
		try:
			mode     = int  (linesplit[0]) 
			affinity = float(linesplit[1]) 
			rmsd_l_b = float(linesplit[2])
			rmsd_u_b = float(linesplit[3])
			output_list.append([ligand_name, receptor_name, mode, affinity, rmsd_l_b, rmsd_u_b])
		
		except:
			pass
	
	return output_list
		

def list_PDBQT_files(folder):
	""" Function doc """
	files   = os.listdir(folder)
	pdbqt_list = []
	for _file in files:
		_file2 = _file.split('.')
		if _file2[1] == 'pdbqt' or _file2[1] == 'PDBQT':
			#print _file
			_file3 = os.path.join(folder, _file)
			pdbqt_list.append(_file3)
	return pdbqt_list



def run_vina_FR ( receptor_folder   = None ,    # PDBQT folder
                  ligands_folder    = None ,    # PDBQT folder
				  output_folder     = None ,
                  parameters        = None ):
					  
	""" Function doc 
		Input:
		--receptor arg             rigid part of the receptor (PDBQT)
		--flex arg                 flexible side chains, if any (PDBQT)
		--ligand arg               ligand (PDBQT)
		
		Search space (required):
		--center_x arg             X coordinate of the center
		--center_y arg             Y coordinate of the center
		--center_z arg             Z coordinate of the center
		--size_x arg               size in the X dimension (Angstroms)
		--size_y arg               size in the Y dimension (Angstroms)
		--size_z arg               size in the Z dimension (Angstroms)
		
		Output (optional):
		--out arg                  output models (PDBQT), the default is chosen based
									on the ligand file name
		--log arg                  optionally, write log file
		
		Misc (optional):
		--cpu arg                  the number of CPUs to use (the default is to try 
									to detect the number of CPUs or, failing that, use
									1)
		--seed arg                 explicit random seed
		--exhaustiveness arg (=8)  exhaustiveness of the global search (roughly 
									proportional to time): 1+
		--num_modes arg (=9)       maximum number of binding modes to generate
		--energy_range arg (=3)    maximum energy difference between the best binding
									mode and the worst one displayed (kcal/mol)
		
		Configuration file (optional):
		--config arg               the above options can be put here
		
		Information (optional):
		--help                     display usage summary
		--help_advanced            display usage summary with advanced options
		--version                  display program version
	"""
	
	
	'''
	parameters = {
		'--receptor'              : None ,        
		'--flex'                  : None ,
		'--ligand'                : None ,
		
		#Search space (required): 
		
		'--center_x'              : None ,
		'--center_y'              : None ,
		'--center_z'              : None ,
		'--size_x'                : None ,
		'--size_y'                : None ,
		'--size_z'                : None ,
		
		#Output (optional): 
		
		'--out'                   : None ,
		'--log'                   : None ,
		
		#Misc (optional):  
		
		'--cpu'                   : None ,
		'--seed'                  : None ,
		'--exhaustiveness'        : None ,
		'--num_modes'             : None ,
		'--energy_range'          : None ,
	           }
	'''
	receptors = list_PDBQT_files(receptor_folder)
	ligands   = list_PDBQT_files(ligands_folder)
	
	
	
	OUTPUTS   = output_folder
	if not os.path.isdir(OUTPUTS):              
		try:
			print "Creating: ", OUTPUTS             
			os.mkdir(OUTPUTS)                       
		except:                               
			print 'Unable to create: ', OUTPUTS
	
	
	
	
	
	
	loglist          = []
	output_list_full = []
	
	
	#------------------------------------------------------------------------------------------------------------------------
	#affinity_logs
	fulllog = open(os.path.join(OUTPUTS, 'affinity_logs.txt'), 'w')
	text = "\n {:10}   {:^30}   {:^10}  {:^15} {:^15} {:^15} ".format('ligand','frame','mode','affinity','rmsd_l.b.','rmsd_u.b')
	fulllog.write(text)
	fulllog.close()
	#------------------------------------------------------------------------------------------------------------------------
	
	for receptor in receptors:
		for ligand in ligands:
			
			receptor_name = os.path.split(receptor)
			receptor_name = receptor_name[-1]
			receptor_name = receptor_name[:-6]
			ligand_name   = os.path.split(ligand)
			ligand_name   = ligand_name[-1]
			ligand_name   = ligand_name[:-6]
			
			#file out
			output_pdbqt = ligand_name + '_' + receptor_name +'_docked.pdbqt'
			#full path fileout
			out = os.path.join(OUTPUTS, output_pdbqt)
			
			output_log = ligand_name + '_' + receptor_name +'_vina.log'
			log = os.path.join(OUTPUTS, output_log)
			loglist.append(log)
			
			
			# building  command line
			cmd =  'vina'
			for tag in parameters:
				if parameters[tag] == None:
					pass
				else:
					cmd += ' ' + tag + ' ' + str(parameters[tag])
			
			cmd += ' --receptor '+ receptor
			cmd += ' --ligand '  + ligand
			#cmd += ' --center_x ' + str(center_x)
			#cmd += ' --center_y ' + str(center_y)
			#cmd += ' --center_z ' + str(center_z)
			#cmd += ' --size_x '    + str(size_x)
			#cmd += ' --size_y '    + str(size_y)
			#cmd += ' --size_z '    + str(size_z)
			cmd += ' --out '       + out                   #obj01.docked.pdbqt
			cmd += ' --log '       + log                   #obj01.vina.log
			#cmd += ' --num_modes ' + '2'
			#cmd += ' --seed 100 '
			
			
			
			try:
				print '\n\n', cmd, '\n\n'
				os.system(cmd)
				output_list = vina_logparser (log, ligand_name, receptor_name)
				for item in output_list:
					output_list_full.append(item)
					
					#------------------------------------------------------------------------------------------------------------------------
					# log file
					fulllog = open(os.path.join(OUTPUTS, 'affinity_logs.txt'), 'a')
					text = "\n {:10}   {:^30}   {:^10}  {:^15} {:^15} {:^15} "  .format(item[0], item[1], item[2], item[3], item[4], item[5])
					fulllog.write(text)
					fulllog.close()
					#------------------------------------------------------------------------------------------------------------------------
			
			except:
				print 'error - ', ligand_name, receptor_name
				
