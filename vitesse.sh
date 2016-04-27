#pin 18 du Raspbery Pi
gpio mode 1 in
mem=0
tours=0
debut=$(date +%s)
while true
do
	mesure=$(date +%s)
	delta=$(($mesure - $debut + 1))
	hall=$(gpio read 1)
	if [ $hall = 0 ] && [ $mem = 0 ]
	then
		tours=$(($tours + 1))
		mem=1

	fi
	if [ $hall = 1 ] && [ $mem = 1 ]
	then
		mem=0
	fi
	if [ $delta = 2 ]
	then
		ms=$(echo "$tours*0.6"|bc -l)
		kmh=$(echo "$ms*3.6"|bc -l)
		#echo $ms
		echo $kmh >vitesse1.txt
		tours=0
		debut=$(date +%s)
		
	fi
done