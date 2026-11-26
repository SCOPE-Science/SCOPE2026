"""Generate the exact two-cycle ring census from integer de Bruijn matrices."""
import csv
from collections import defaultdict
from verify import graph, characteristic_zeta_denominator, traces, canonical_ratio

pairs = defaultdict(list)
ratios = defaultdict(list)
rows=[]
for r in range(256):
 M1, M2 = graph(r, 1), graph(r, 2)
 D = characteristic_zeta_denominator(M1)
 E = characteristic_zeta_denominator(M2)
 c1, c2 = traces(M1, 6), traces(M2, 6)
 first = next((i+1 for i in range(6) if c2[i]>c1[i]), None)
 assert first is not None or D == E
 pairs[(tuple(D),tuple(E))].append(r)
 ratio = canonical_ratio(D,E)
 ratios[ratio].append(r)
 rows.append((r, D, E, first, ratio))
identifiers={key:idx+1 for idx,key in enumerate(sorted(pairs,key=lambda t:min(pairs[t])))}
ratio_identifiers={key:idx+1 for idx,key in enumerate(sorted(ratios,key=lambda t:min(ratios[t])))}
with open('eca2_rules.csv','w',encoding='utf-8',newline='') as fh:
 writer=csv.writer(fh)
 writer.writerow(['rule','class_id','ratio_class_id','fixed_denominator_coefficients','second_fixed_denominator_coefficients','first_two_cycle_ring'])
 for r,D,E,first,ratio in rows:
  writer.writerow([r,identifiers[(tuple(D),tuple(E))],ratio_identifiers[ratio],str(D),str(E),first if first else ''])
with open('eca2_classes.csv','w',encoding='utf-8',newline='') as fh:
 writer=csv.writer(fh)
 writer.writerow(['class_id','multiplicity','rules','fixed_denominator_coefficients','second_fixed_denominator_coefficients'])
 for key,ident in sorted(identifiers.items(),key=lambda x:x[1]):
  D,E=key
  writer.writerow([ident,len(pairs[key]),str(pairs[key]),str(list(D)),str(list(E))])
with open('eca2_ratio_classes.csv','w',encoding='utf-8',newline='') as fh:
 writer=csv.writer(fh)
 writer.writerow(['ratio_class_id','multiplicity','rules','numerator_coefficients','denominator_coefficients'])
 for key,ident in sorted(ratio_identifiers.items(),key=lambda x:x[1]):
  num,den=key
  writer.writerow([ident,len(ratios[key]),str(ratios[key]),str(list(num)),str(list(den))])
print('TABLES_OK',len(pairs),len(ratios),len(rows))
