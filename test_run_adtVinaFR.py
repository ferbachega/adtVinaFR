from adtFRcore import *


#center_x  = 53.29
#center_y  = 45.49
#center_z  = 75.09
#size_x    = 25.12
#size_y    = 27.75
#size_z    = 24.75
##out       =  '/h
##log       =  '/h
#num_modes =  10


parameters = {
		#'--receptor'              : None ,        
		#'--flex'                  : None ,
		#'--ligand'                : None ,
		
		#Search space (required): 
		
		'--center_x'              : 53.29 ,
		'--center_y'              : 45.49 ,
		'--center_z'              : 75.09 ,
		'--size_x'                : 25.12 ,
		'--size_y'                : 27.75 ,
		'--size_z'                : 24.75 ,
		
		#Output (optional): 
		
		#'--out'                   : None ,
		#'--log'                   : None ,
		
		#Misc (optional):  
		
		'--cpu'                   : None ,
		'--seed'                  : None ,
		'--exhaustiveness'        : None ,
		'--num_modes'             : 2    ,
		'--energy_range'          : None ,
		
		 }

receptor_folder   =  '/home/fernando/programs/adtVinaFR/flexible_receptor_PDB'
ligands_folder    =  '/home/fernando/programs/adtVinaFR/ligands_PDB'
output_folder     =  '/home/fernando/programs/adtVinaFR/OUTPUTS'


run_vina_FR ( receptor_folder   = receptor_folder,    # PDBQT folder
              ligands_folder    = ligands_folder ,    # PDBQT folder
              output_folder     = output_folder  ,
              parameters        = parameters     )
              
              
              
