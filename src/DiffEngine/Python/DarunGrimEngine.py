import sys
import DiffEngine
import os

class Differ:
	def __init__ ( self ):
		pass

	def DiffFile( self, TheSourceFilename, TheTargetFilename, StorageFilename, LogFilename, IDAPath = r'C:\Program Files (x86)\IDA\idag.exe' ):
		TheSourceFilename = str(TheSourceFilename)
		TheTargetFilename = str(TheTargetFilename)
		#print 'Comparing',TheSourceFilename,TheTargetFilename

		StorageFilename = os.path.join( os.getcwd(), str(StorageFilename) )
		LogFilename = os.path.join( os.getcwd(), str(LogFilename) )

		self.DarunGrim = DiffEngine.DarunGrim()
		self.DarunGrim.SetIDAPath( IDAPath )
		self.DarunGrim.GenerateDB(
			StorageFilename, LogFilename, 
			TheSourceFilename, 0, 0,
			TheTargetFilename, 0, 0)
		self.DarunGrim.Analyze()

	def SyncIDA( self ):
		self.DarunGrim.AcceptIDAClientsFromSocket()

if __name__ == '__main__':
	"""
	TheSourceFilename = sys.argv[1]
	TheTargetFilename = sys.argv[2]
	StorageFilename = sys.argv[3]

	LogFilename = 'test.log'

	IDAPath = r'C:\Program Files (x86)\IDA\idag.exe'
	DiffFile( TheSourceFilename, TheTargetFilename, StorageFilename, LogFilename, IDAPath )
	"""
	
	"""
	ida_client_manager = DiffEngine.IDAClientManager()
	ida_client_manager.StartIDAListener( 1216 )
	"""
	
	darun_grim = DiffEngine.DarunGrim()
	storage_filename = os.path.join( os.getcwd(), str('test2.dgf') )
	darun_grim.AcceptIDAClientsFromSocket( storage_filename )
	raw_input( 'Press any key to continue...' )
