import pickle, time
with open("ord_d2.pkl","rb") as f:
    D=pickle.load(f)
rows_list=D["rows"]; vals_list=D["vals"]; R=D["nrows"]; C=D["ncols"]
row_cols=[[] for _ in range(R)]
row_vals=[[] for _ in range(R)]
for j in range(C):
    for r,v in zip(rows_list[j],vals_list[j]):
        row_cols[r].append(j); row_vals[r].append(v)
def rank_mod_row(p):
    rws=[dict(zip(a,b)) for a,b in zip(row_cols,row_vals)]
    for d in rws:
        for k in list(d):
            d[k]%=p
            if d[k]==0: del d[k]
    cpiv={}; rank=0
    t0=time.time()
    for r in range(R):
        d=rws[r]
        while d:
            c=min(d)
            q=cpiv.get(c)
            if q is None: break
            prow=rws[q]; f=d[c]
            for cc,vv in prow.items():
                nv=(d.get(cc,0)-f*vv)%p
                if nv: d[cc]=nv
                elif cc in d: del d[cc]
        if d:
            c=min(d)
            inv=pow(d[c],-1,p)
            for cc in list(d): d[cc]=(d[cc]*inv)%p
            cpiv[c]=r; rank+=1
    print("rank",rank,"time",time.time()-t0,flush=True)
    return rank
for p in [1000003, 7]:
    print("p=",p,flush=True)
    print(rank_mod_row(p),flush=True)
