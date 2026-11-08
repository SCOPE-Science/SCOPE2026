"""Run and independently compare the two exhaustive finite-state certificates.
Usage: python3 verify.py (requires C++17 compiler g++).
"""
import json
import subprocess
import sys
from pathlib import Path

base=Path(__file__).resolve().parent
subprocess.run(['g++','-O2','-std=c++17','-o',str(base/'census_cpp_exec'),str(base/'census_cpp.cpp')],check=True)
cpp=json.loads(subprocess.check_output([str(base/'census_cpp_exec')],cwd=base,text=True))
py=json.loads(subprocess.check_output([sys.executable,str(base/'census_python.py')],cwd=base,text=True))
for name,data,expectedfile in [('cpp',cpp,'census_cpp.json'),('python',py,'census_python.json')]:
    saved=json.loads((base/expectedfile).read_text(encoding='utf-8'))
    assert data==saved, f'{name}: replay differs from recorded exact output'
for field in ('cycle_counts','basin_counts','time_period_counts','max_transient','max_transient_population'):
    assert cpp[field]==py[field],field
for L in ('4','6','8'):
    A=cpp['long_cycle_orbits'][L]
    B=py['long_cycle_orbits'][L]
    assert len(A)==len(B)==1,(L,'orbits')
    for item in ('representative','size','stabilizer','profile','cycle_representatives'):
        assert A[0][item]==B[0][item],(L,item)
assert cpp['cycle_counts']=={'1':1,'3':3108,'4':6,'6':12,'8':6}
assert cpp['basin_counts']=={'1':52677,'3':340848,'4':4656,'6':127116,'8':6144}
assert sum(cpp['basin_counts'].values())==3**12
assert sum(int(p)*n for p,n in cpp['cycle_counts'].items())==9469
assert cpp['max_transient']==10 and cpp['max_transient_population']==384
assert sum(n for p,t,n in cpp['time_period_counts'] if t==0)==9469
assert sum(n for p,t,n in cpp['time_period_counts'] if t==10)==384
for L,sz,stab,pervertex in [('4',6,4,1),('6',12,2,1),('8',6,4,2)]:
    o=py['long_cycle_orbits'][L][0]
    assert (o['size'],o['stabilizer'])==(sz,stab)
    assert o['vertex_excitation_counts']==[pervertex]*12
print('VERIFY_OK: all 531441 states, all periods/transients, two algorithmic methods, all 24 spatial permutations, long-orbit profiles')
