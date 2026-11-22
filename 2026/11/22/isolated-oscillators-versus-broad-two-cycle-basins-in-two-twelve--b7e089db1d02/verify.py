#!/usr/bin/env python3
"""Replay exact finite certificates; needs Python 3.9+ and a C++17 compiler."""
import json, pathlib, subprocess, tempfile
base=pathlib.Path(__file__).resolve().parent
result=subprocess.run(['python3',str(base/'archimedean_majority.py')],cwd=base,capture_output=True,text=True,check=True)
actual=json.loads((base/'archimedean_census.json').read_text())
expected=json.loads((base/'reference_census.json').read_text())
assert json.loads(result.stdout)==actual==expected
pairs=[('truncated_tetrahedron',16,239,26,5,2366,1360),('cuboctahedron',146,20,3,4,40,2064)]
for name,fixed,orbits,geo,depth,two_basin,consensus in pairs:
 d=actual[name]
 assert (d['fixed'],d['primitive_two_orbits'],d['primitive_two_spatial_classes'],d['sharp_first_entry_time'],d['basin_population']['2'],sum(d['consensus_basin_per_color']))==(fixed,orbits,geo,depth,two_basin,consensus)
 assert sum(map(int,d['entry_time_histogram'].values()))==4096
 assert sum(map(int,d['basin_population'].values()))==4096
 assert sum(int(t)*int(count) for t,count in d['primitive_two_spatial_size_histogram'].items())==orbits
 assert sum(int(t)*int(count) for t,count in d['fixed_spatial_size_histogram'].items())==fixed
assert actual['cuboctahedron']['first_entry_period_histogram']['2']=={'0':40}
assert actual['truncated_tetrahedron']['first_entry_period_histogram']['2']=={'0':478,'1':1264,'2':528,'3':96}
with tempfile.TemporaryDirectory() as td:
 exe=str(pathlib.Path(td)/'check')
 subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra','-pedantic',str(base/'archimedean_independent.cpp'),'-o',exe],check=True,capture_output=True,text=True)
 check=subprocess.run([exe],check=True,capture_output=True,text=True)
 assert check.stdout.endswith('INDEPENDENT_CERTIFICATE_OK\n')
 for name,fix,cyc,_,_,two_basin,consensus in pairs:
  assert any(line.startswith(name+' fixed='+str(fix)+' two_orbits='+str(cyc)) and ('two_basin='+str(two_basin)) in line and ('consensus_basin='+str(consensus)) in line for line in check.stdout.splitlines())
 print(check.stdout.strip())
print('VERIFY_OK')
