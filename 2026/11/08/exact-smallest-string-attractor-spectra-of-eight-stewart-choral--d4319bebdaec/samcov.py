import time

def word(k):
 w='0'
 for _ in range(k):w=''.join('001' if x=='0' else '011' for x in w)
 return w

def covers(w):
 edges=[{}];link=[-1];length=[0];end=[0];last=0
 for i,c in enumerate(w):
  cur=len(edges);edges.append({});length.append(length[last]+1);link.append(0);end.append(1<<i)
  p=last
  while p>=0 and c not in edges[p]: edges[p][c]=cur;p=link[p]
  if p>=0:
   q=edges[p][c]
   if length[p]+1==length[q]:link[cur]=q
   else:
    clone=len(edges);edges.append(edges[q].copy());length.append(length[p]+1);link.append(link[q]);end.append(0)
    while p>=0 and edges[p].get(c)==q:edges[p][c]=clone;p=link[p]
    link[q]=link[cur]=clone
  last=cur
 for v in sorted(range(1,len(edges)),key=lambda v:length[v],reverse=True):end[link[v]] |=end[v]
 covers=[]
 for v in range(1,len(edges)):
  L=length[link[v]]+1
  mask=end[v]
  h=1
  while 2*h<=L:
   mask|=mask>>h;h*=2
  if L>h:mask|=mask>>(L-h)
  covers.append(mask)
 covers=sorted(set(covers),key=int.bit_count)
 mins=[]
 for m in covers:
  if not any((x&m)==x for x in mins): mins.append(m)
 return mins,len(edges),len(covers)
