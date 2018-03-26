BEGIN {

printf " %8s %11s\n" , "User Name" , "Login Date"
print "==========================="

}

!(/Never logged in/ || /^Username/ ) {
cn++

if ( NF == 8 )
   printf "%8s %2s %3s %4s\n" , $1,$5,$4,$8,$3

else
   printf "%8s %2s %3s %4s\n" , $1,$6,$5,$9,$3
}
END {
print "===================="

print "Total Number of Uers processed: " , cn
}










