## census96_clean.g — clean rerun with long lines to avoid CSV wrapping
SizeScreen([10000, 24]);
SetPrintFormattingStatus("*stdout*", false);
Print("GAP version: ", GAPInfo.Version, "\n");
Print("SmallGrp version: ", GAPInfo.PackagesLoaded.smallgrp[2], "\n");
Print("SmallGrp path: ", GAPInfo.PackagesLoaded.smallgrp[1], "\n");
Print("Timestamp start: ", StringTime(NanosecondsSinceEpoch()), "\n");
Print("NumberSmallGroups(96) = ", NumberSmallGroups(96), "\n");
outfile := "output/artifacts/census96.csv";
PrintTo(outfile, "i,desc,s,k,isAbelian,profile\n");
for i in [1..231] do
  G := SmallGroup(96, i);
  L := LatticeSubgroups(G);
  ccs := ConjugacyClassesSubgroups(L);
  s := Sum(ccs, Size);
  k := Length(ConjugacyClasses(G));
  ab := IsAbelian(G);
  desc := StructureDescription(G);
  if desc = fail then
    desc := Concatenation("IdGroup[96,", String(i), "]");
  fi;
  orders := Set(List(ccs, c -> Order(Representative(c))));
  Sort(orders);
  profstr := "";
  for o in orders do
    tot := Sum(Filtered(ccs, c -> Order(Representative(c)) = o), Size);
    if profstr <> "" then profstr := Concatenation(profstr, "|"); fi;
    profstr := Concatenation(profstr, String(o), ":", String(tot));
  od;
  desc2 := ReplacedString(desc, ",", ";");
  desc2 := ReplacedString(desc2, "\"", "'");
  AppendTo(outfile, String(i), ",\"", desc2, "\",", String(s), ",", String(k), ",", String(ab), ",\"", profstr, "\"\n");
  Print(i, ": s=", s, " k=", k, " ab=", ab, " ", desc2, "\n");
od;
Print("Timestamp end: ", StringTime(NanosecondsSinceEpoch()), "\n");
Print("CENSUS DONE\n");
QUIT;
