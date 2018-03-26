import subprocess
p = subprocess.Popen(["cat", "/etc/resolv.conf" ], stdout=subprocess.PIPE)
#p = subprocess.Popen(["ping", "-c", "10", "127.0.0.1"], stdout=subprocess.PIPE)
output, err = p.communicate()
print  output

#q = subprocess.Popen(["sed",  "s/name/10.157.68.10/gi" ,output], stdout=subprocess.PIPE)
q = subprocess.Popen(["sed",  "s/name/10.157.68.10/gi" ,"<" ,output], stdout=subprocess.PIPE)


output, err = q.communicate()
print  output
