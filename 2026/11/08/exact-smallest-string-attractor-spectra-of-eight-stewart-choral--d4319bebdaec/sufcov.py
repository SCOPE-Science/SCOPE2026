
def suffix_tree_masks(w):
 n=len(w)
 sa=sorted(range(n),key=lambda i:w[i:])
 rank=[0]*n
 for q,p in enumerate(sa):rank[p]=q
 lcp=[0]*n;h=0
 for i in range(n):
  if rank[i]==0:h=0;continue
  j=sa[rank[i]-1]
  while i+h<n and j+h<n and w[i+h]==w[j+h]:h+=1
  lcp[rank[i]]=h
  if h:h-=1
 # node=[depth,children,occstart,parent]
 nodes=[[0,[],0,-1]]
 stack=[0]
 for i,p in enumerate(sa):
  v=lcp[i]
  while nodes[stack[-1]][0]>v:stack.pop()
  if nodes[stack[-1]][0]<v:
   parent=stack[-1]
   old=nodes[parent][1].pop()
   new=len(nodes)
   nodes.append([v,[old],0,parent])
   nodes[old][3]=new
   nodes[parent][1].append(new)
   stack.append(new)
  parent=stack[-1]
  leaf=len(nodes);nodes.append([n-p,[],1<<p,parent]);nodes[parent][1].append(leaf)
  stack.append(leaf)
 for v in sorted(range(1,len(nodes)),key=lambda x:nodes[x][0],reverse=True):
  par=nodes[v][3]
  nodes[par][2]|=nodes[v][2]
 out=[]
 for i in range(1,len(nodes)):
  d,ch,S,p=nodes[i]
  L=nodes[p][0]+1
  if d<L:continue
  x=S;h=1
  while 2*h<=L:x|=x<<h;h*=2
  if L>h:x|=x<<(L-h)
  out.append(x)
 out=sorted(set(out),key=int.bit_count)
 mins=[]
 for x in out:
  if not any(y&x==y for y in mins):mins.append(x)
 return mins,len(nodes)
