"""Substep 5: stable turn sets via deep iteration (fixpoint)."""
def inv(d): return d+5 if d<5 else d-5
def neg(w): return tuple(inv(d) for d in reversed(w))
def red(w):
    st=[]
    for d in w:
        if st and st[-1]==inv(d): st.pop()
        else: st.append(d)
    return tuple(st)
def show(d): return ('a' if d<5 else 'A')+str((d%5)+1)
def apply(f,w):
    out=[]
    for d in w:
        out.extend(f[d] if d<5 else neg(f[d-5]))
    return red(tuple(out))
f_phi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,1,2)}
f_psi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,2,1)}
def stable_turns(f,depth):
    cur={i:tuple(f[i]) for i in range(5)}
    taken=set()
    for k in range(depth):
        for i in range(5):
            w=cur[i]
            for a,b in zip(w,w[1:]):
                taken.add(tuple(sorted((inv(a),b))))
        cur={i:apply(f,cur[i]) for i in range(5)}
    return taken
for depth in [6,10,15,20,25,30]:
    tp=stable_turns(f_phi,depth); ts=stable_turns(f_psi,depth)
    print(depth,'phi:',len(tp),'psi:',len(ts))
tp=stable_turns(f_phi,30); ts=stable_turns(f_psi,30)
import json
def s(t): return sorted([[show(a),show(b)] for a,b in t])
json.dump({'phi':s(tp),'psi':s(ts)},open('output/artifacts/stable_turns.json','w'))
print('PHI:',s(tp)); print('PSI:',s(ts))
# connectivity + degree seq
def conn(t):
    adj={d:set() for d in range(10)}
    for a,b in t: adj[a].add(b); adj[b].add(a)
    seen={0};st=[0]
    while st:
        x=st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y);st.append(y)
    return len(seen)==10,sorted(len(adj[d]) for d in range(10))
print('phi conn,degseq:',conn(tp)); print('psi conn,degseq:',conn(ts))
