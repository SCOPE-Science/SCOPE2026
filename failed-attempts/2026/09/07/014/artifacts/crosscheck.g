## crosscheck.g — independent recomputation
SizeScreen([10000, 24]);
SetPrintFormattingStatus("*stdout*", false);
Print("GAP ", GAPInfo.Version, " SmallGrp ", GAPInfo.PackagesLoaded.smallgrp[2], "\n");
# top-10 by s from census
top10 := [230, 231, 207, 209, 219, 228, 229, 226, 206, 216];
# also all k=60 ids for k cross-check
k60 := [45,47,48,55,60,162,163,164,165,166,177,178,221,222,223];
Print("=== s cross-check via AllSubgroups ===\n");
for i in top10 do
  G := SmallGroup(96, i);
  L := LatticeSubgroups(G);
  ccs := ConjugacyClassesSubgroups(L);
  s1 := Sum(ccs, Size);
  all := AllSubgroups(G);
  s2 := Length(all);
  # third route: subgroup-conjugacy expansion = sum of class sizes (same as s1 but recompute sizes via Orbit?)
  Print("i=", i, " s_lattice=", s1, " s_AllSubgroups=", s2, " match=", s1=s2, "\n");
od;
Print("=== k cross-check via CharacterTable / Irr ===\n");
for i in Union(top10, k60) do
  G := SmallGroup(96, i);
  k1 := Length(ConjugacyClasses(G));
  ct := CharacterTable(G);
  k2 := NrConjugacyClasses(ct);
  k3 := Length(Irr(G));
  Print("i=", i, " k_classes=", k1, " k_chartab=", k2, " k_Irr=", k3, " match=", (k1=k2 and k1=k3), "\n");
od;
# global re-verification of maxima from scratch (no CSV): loop and track max
Print("=== global max rescan ===\n");
Smax := 0; Sids := [];
Kmax := 0; Kids := [];
for i in [1..231] do
  G := SmallGroup(96, i);
  s := Sum(ConjugacyClassesSubgroups(LatticeSubgroups(G)), Size);
  k := Length(ConjugacyClasses(G));
  if s > Smax then Smax := s; Sids := [i]; elif s = Smax then Add(Sids, i); fi;
  if not IsAbelian(G) then
    if k > Kmax then Kmax := k; Kids := [i]; elif k = Kmax then Add(Kids, i); fi;
  fi;
od;
Print("Smax=", Smax, " Sids=", Sids, "\n");
Print("Kmax(nonab)=", Kmax, " Kids=", Kids, "\n");
Print("CROSSCHECK DONE\n");
QUIT;
