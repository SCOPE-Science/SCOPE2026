"""Offline one-command replay: from replay_inputs.json (PD + atlas Jones per knot),
recompute Jones by BOTH methods and require exact agreement. No network needed.
Run: python3 output/artifacts/verify_offline.py  (from the lane root)."""
import sys, os, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jones_engine import parse_pd, jones_both
def parse4(s):
    s=s.replace(' ','')
    if s and s[0] not in '+-': s='+'+s
    t=s.replace('^-','^~'); d={}
    for p in re.findall(r'[+-][^+-]+',t):
        p=p.replace('^~','^-'); sg=1 if p[0]=='+' else -1; body=p[1:]
        if 'q' not in body: d[0]=d.get(0,0)+sg*int(body)
        else:
            m=re.match(r'(?:(\d+)\*?)?q(?:\^(-?\d+))?$',body); assert m,body
            c=int(m.group(1)) if m.group(1) else 1; e=int(m.group(2)) if m.group(2) else 1
            d[e]=d.get(e,0)+sg*c
    return {e:c for e,c in d.items() if c}
inp=json.load(open(os.path.join(HERE,'replay_inputs.json')))
n=ok=0
for lab,v in sorted(inp.items()):
    pd=parse_pd(v['PD']); w,V,br=jones_both(pd); n+=1
    a=parse4(v['atlas'].replace('\\displaystyle','').replace('{','').replace('}','').replace('\\',''))
    assert {int(e):c for e,c in V.items()}==a, lab
    ok+=1
print(f"OFFLINE VERIFY PASS: {ok}/{n} two-method + atlas agreement")
