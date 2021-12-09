#aafgen: amino acid fragments gen
#gen is postfix for all related programs
if [ $# -ne 2 ]; then
	echo "Usage: aafrgen.sh <file> <restriction>" 
	exit 1
fi

is_genomial=$(./chkgen.py $1)
if [ "$is_genomial" != "is genomial" ]; then
	echo "fatal: sequence isn't genomial"
	exit 1
fi

res=$(./cutgen.py $1 $2 | tee /dev/tty)
fragments=$(echo "$res" | awk '{print $2}' | tail -n +2)
echo ""
for j in $fragments; do
	echo $j
	./proteingen.py $j
	echo ""
done

