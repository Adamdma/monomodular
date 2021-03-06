# by amounra 0513 : http://www.aumhaa.com

from Codex import Codex

def create_instance(c_instance):
	""" Creates and returns the Codec script """
	return Codex(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[115], model_name='Livid Instruments Code'),
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SCRIPT, REMOTE])]}