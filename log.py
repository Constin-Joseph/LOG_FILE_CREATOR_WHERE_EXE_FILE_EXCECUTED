import logging
import os
def logerr(e):
    pat=os.getcwd()
    pathh= os.path.join(pat, 'log_file_name.log')
    logging.basicConfig(filename=pathh, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logger=logging.getLogger(__name__)
    logger.error(e)
    print("log file created",pathh)
logerr(e)#call in main program
#pass any program exception here(i.e)except exception as e:


