from pc import Zeeman
from pc import FDMesh
from pc import Sim
import numpy as np

def varying_field(pos):
    return (1.2*pos[0],2.3*pos[1],0)

def test_zeeman():
    
    mesh=FDMesh(nx=5,ny=2,nz=1)
    
    sim=Sim(mesh)
    sim.set_m((1,0,0))
    
    zeeman = Zeeman(varying_field)
    sim.add(zeeman)
    
    field = zeeman.compute_field()

    assert field[4]==1.2*2
    assert field[14]==2.3*0

    
    
if __name__=='__main__':
    test_zeeman()
    
