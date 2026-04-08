import os,re
for root,dirs,files in os.walk('.'):
 for f in files:
  if not f.endswith('.md'):continue
  path=os.path.join(root,f)
  lines=open(path,encoding='utf-8').readlines()
  for i,line in enumerate(lines):
   if re.match(r'^#{1,6} ',line) and i+1<len(lines) and lines[i+1].strip()!='':
    print(path+':'+str(i+1)+': '+line.rstrip())

