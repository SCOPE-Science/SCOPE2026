"""Independent combinatorial fixed-weight formulas for two odd prime factors."""
from math import comb
from collections import Counter
import subprocess, re, tempfile, pathlib

def expected(p,q):
    n=p*q
    rank_count=Counter()
    weight_counts={}
    for k in range(n+1):
        d=Counter()
        if k in (0,n):
            d[1]=1
        else:
            if k%q==0:
                a=k//q
                d[p]=comb(p,a)
                d[n-q+1]=comb(p,a)**q-comb(p,a)
            if k%p==0:
                b=k//p
                d[q]=comb(q,b)
                d[n-p+1]=comb(q,b)**p-comb(q,b)
            d[n]=comb(n,k)-sum(d.values())
        assert all(v>=0 for v in d.values()),(p,q,k,d)
        assert sum(d.values())==comb(n,k)
        rank_count.update(d)
        weight_counts[k]=d
    return rank_count,weight_counts

with tempfile.TemporaryDirectory() as scratch:
    root = pathlib.Path(__file__).resolve().parent
    binary = pathlib.Path(scratch) / 'cyc_rank_exact'
    subprocess.run(['g++','-O2','-std=c++17',str(root/'cyclotomic_rank_census.cpp'),'-o',str(binary)], check=True)
    for p,q in ((3,5),(3,7)):
        ex,ew=expected(p,q)
        out=subprocess.check_output([str(binary),str(p),str(q)],text=True)
        line=out.splitlines()[0]
        seen=Counter({int(r):int(c) for r,c in re.findall(r'(\d+):(\d+)',line)})
        assert ex==seen,(p,q,ex,seen)
        for s in out.splitlines()[1:]:
            k=int(s.split(':')[0].split()[1]); d=Counter({int(r):int(c) for r,c in re.findall(r'(\d+)=(\d+)',s)})
            assert ew[k]==d,(p,q,k,ew[k],d)
        print(line)
        print('Fixed-weight counts: independently match at all',p*q+1,'Hamming weights')
print('ALL EXACT CHECKS PASSED')
