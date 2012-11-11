autowatch = 1;

inlets = 3;
outlets = 3;
setinletassist(0, 'live.this_device input');
setinletassist(1, 'slot, offset, pattrstorage, alt input');
setinletassist(2, 'grid input');
setoutletassist(0, 'preset data grid output');
setoutletassist(1, 'gate value output');
setoutletassist(2, 'main data grid output');

var args1 = jsarguments[1];
var alive = 0;
var storage;// = this.patcher.getnamed('boiingg');
var preset_selector;// = this.patcher.getnamed('preset_selector');
var s_offset = [0, 0];
var preset = 0;
var alt = 0;
const empty = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];

function init()
{
	alive = 1;
	storage = this.patcher.getnamed(args1);
	preset_selector = this.patcher.getnamed('preset_selector');
}

function alt(value)
{
    if(value == 1)
    {    
        outlet(0, 0);
        outlet(1, 'clear');
    }
}

function surface_offset(x, y)
{
	//post('plinko offset', x, y, '\n');
	s_offset = [x, y];
}

function list(x, y, z)
{
	if(alive > 0)
	{
		if(alt > 0)
		{
			if(z>0)
			{
				//post('alt press', x, y, s_offset[0], s_offset[1], '\n');
				if(y < (4 + s_offset[1]))
				{	
					//post((x-s_offset[0]) + (y-(s_offset[1]*8)), 'recall', '\n');
					preset_selector.message((x-s_offset[0]) + ((y-s_offset[1])*8) +1);
				}
				else
				{
					//post('store', (x-s_offset[0]) + ((y-(s_offset[1])-4)*8) +1);
					preset_selector.message('store', (x-s_offset[0]) + (((y-s_offset[1])-4)*8) +1);
				}
				storage.message('getslotlist');
			}
		}
		else
		{
			outlet(2, x, y, z);
		}
	}
}

function slot(val)
{
	preset = val;
}

function slotlist()
{
	args = arrayfromargs(arguments);
	//post('slotlist', args, '\n');
	var loaded = empty.slice();
	if(alt>0)
	{
		for(var i=0;i<args.length;i++)
		{
			outlet(0, (args[i]-1)%8 + s_offset[0], Math.floor((args[i]-1)/8) + s_offset[1], (1 + (args[i]==preset)));
			//post(0, (args[i]-1)%7 + s_offset[0], Math.floor((args[i]-1)/7) + s_offset[1], 1, '\n');
			loaded[args[i]-1] = 0;
		}
		for(var j=0;j<4;j++)
		{
			for(var k=0;k<8;k++)
			{
				outlet(0, k, j+4, loaded[((j*8)+k)]);
			}
		}
	}
} 

function msg_int(key)
{
	if(alive > 0)
	{
		if(inlet == 1)
		{
			alt=key;
			if(key<1)
			{
				outlet(0, 'clear');
				outlet(1, 1);
			}
			else
			{
				outlet(1, 0);
				outlet(0, 'clear');
				storage.message('getslotlist');
			}
		}
	}	
}

function anything()
{
	return;
}

function bang()
{
	if(inlet == 0)
	{
		init();
	}
}