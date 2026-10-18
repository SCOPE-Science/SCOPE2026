#!/usr/bin/env python3
import json, pathlib, subprocess, tempfile
from collections import deque
root=pathlib.Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
with tempfile.TemporaryDirectory() as td:
    exe=pathlib.Path(td)/"census"
    subprocess.run(["g++","-O3","-march=native","-std=c++17",str(root/"census.cpp"),"-o",str(exe)],check=True)
    p=subprocess.run([str(exe)],capture_output=True,text=True,check=True,timeout=90)
assert p.stdout.startswith("VERIFY_OK sizes=2..8"),p.stdout

a=(0,0,3,5,1,2,6,7)
b=(1,2,3,4,5,6,7,0)
target=frozenset((0,1,2,4,5,6))
full=frozenset(range(8))
def image(S,t): return frozenset(t[q] for q in S)
q=deque([full]); dist={full:0}; parent={full:None}; edge={}
while q:
    S=q.popleft()
    for ch,t in (("a",a),("b",b)):
        U=image(S,t)
        if U not in dist:
            dist[U]=dist[S]+1;parent[U]=S;edge[U]=ch;q.append(U)
assert len(dist)==255
assert dist[target]==17
w=[];S=target
while S!=full:
    w.append(edge[S]);S=parent[S]
w=''.join(reversed(w))
assert w=="abbbbbbabbbbbabbb"
T=full
for ch in w:T=image(T,a if ch=="a" else b)
assert T==target
viol=[]
for S,d in dist.items():
    if d>8*(8-len(S)):viol.append((tuple(sorted(S)),d,8*(8-len(S))))
assert viol==[((0,1,2,4,5,6),17,16)]
print(p.stdout.strip())
print("REPRESENTATIVE_OK distance=17 target=012456 word=abbbbbbabbbbbabbb all_nonempty_subsets_reached=255 unique_violation=1")
