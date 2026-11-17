"""Reproduce the complete integral discrete-Morse certificate for a pentagonal four-row cylinder."""
import json,os,subprocess,hashlib,pathlib,tempfile
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
BASE=pathlib.Path(__file__).resolve().parent

def call(args,cwd):
 p=subprocess.run(args,cwd=cwd,text=True,capture_output=True,check=True)
 return p.stdout,p.stderr

def run(seed):
 with tempfile.TemporaryDirectory(prefix='cyl_matching_') as tmp:
  tmp=pathlib.Path(tmp)
  for name in ('enumerate.cpp','check_acyclic.cpp','build_morse.py'):
   (tmp/name).write_bytes((BASE/name).read_bytes())
  call(['g++','-O3','-std=c++17','enumerate.cpp','-o','enumerate'],tmp)
  call(['g++','-O3','-std=c++17','check_acyclic.cpp','-o','check_acyclic'],tmp)
  out,gen=call(['./enumerate','4','5',str(seed)],tmp)
  acyclic,_=call(['./check_acyclic'],tmp)
  assert 'faces=253880 matching_pairs=' in acyclic
  assert 'cover_relations=1574120' in acyclic
  assert 'topological_sorted=253880 acyclic=1' in acyclic
  assert 'faces incl empty 253880' in gen
  assert 'fvector -1:1 0:35 1:505 2:3910 3:17725 4:48193 5:77405 6:69510 7:31060 8:5360 9:176' in gen
  _,morse=call(['python','build_morse.py'],tmp)
  data=json.loads((tmp/'morse_matrices.json').read_text())
  A=sp.Matrix(data['6']['rows']).T
  B=sp.Matrix(data['7']['rows']).T
  assert A*B==sp.zeros(A.rows,B.cols)
  def smith(M):
   S=smith_normal_form(M,domain=ZZ)
   return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
  factors_A=smith(A);factors_B=smith(B)
  assert all(x==1 for x in factors_A+factors_B)
  h6=A.cols-len(factors_A)-len(factors_B)
  h7=B.cols-len(factors_B)
  assert (h6,h7)==(141,5)
  return dict(seed=seed,acyclic=acyclic.strip(),critical=gen.strip().split('critical ')[-1].splitlines()[0],boundary_6_shape=list(A.shape),boundary_7_shape=list(B.shape),smith_6=factors_A,smith_7=factors_B,homology_6=h6,homology_7=h7)

if __name__=='__main__':
 for seed in (138,1):
  x=run(seed)
  print(json.dumps(x,separators=(',',':'),sort_keys=True))
 print('VERIFIED: integral homotopy type is wedge of 141 S^6 and 5 S^7')
