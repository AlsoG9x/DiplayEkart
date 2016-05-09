#pin 16
gpio mode 4 in
while true
do
	battery_raw=$(gpio read 1)
	battery=$(echo "$battery_raw/1023*100" | bc -l )
	echo $battery > battery.txt
done
