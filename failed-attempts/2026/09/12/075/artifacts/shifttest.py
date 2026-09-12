from validate_ops import WGraph, build_aztec_cj, brute_Z
def spider_shift(G, corners, s):
    v0,v1,v2,v3=corners
    ws=[]
    for (x,y) in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
        ws.append(G.E.pop(tuple(sorted((x,y)))))
    Delta=ws[0]*ws[2]+ws[1]*ws[3]
    Pts=[]
    for k,vk in enumerate(corners):
        p=('Q',k); G.V[p]=1-G.V[vk]; Pts.append(p)
    for k,vk in enumerate(corners):
        G.add_edge(vk,Pts[k],1.0)
    W=[ws[(k+s)%4]/Delta for k in range(4)]
    for k in range(4):
        G.add_edge(Pts[k],Pts[(k+1)%4],W[k])
    return Delta
for s in [0,1,2,3]:
    G=build_aztec_cj(2,0.7,1.3)
    z0=brute_Z(G)
    corners=[('B',(0,1)),('W',(1,0)),('B',(2,1)),('W',(1,2))]
    D=spider_shift(G,corners,s)
    z1=brute_Z(G)
    print(f"shift={s}: Z0={z0:.9f} D*Z1={D*z1:.9f} ok={abs(z0-D*z1)<1e-9}")
