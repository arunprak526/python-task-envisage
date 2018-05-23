print "\nWelcome to the game AVENGERS ASSEMBLE!!!"
print "\nRules:"
print "1.This game basically forms a team of 4 avengers from a given master set of 10 avengers to fight against thanos."
print "2.It gets the name of 2 avengers from the player and then randomly chooses the other two avengers.(Algorithm is set in order to make sure that all the avengers are different.)"
print "3.Make sure you enter the name of avengers as given on the list, otherwise thanos may succeed."
print "4.Then individual skill set of the chosen 4 avengers are determined from a pre determined set. This follows from their strengths from Marvel Cinematic Universe {MCU}"
print "5.On the other hand, skill set of thanos is determined randomly from a range of values. So, each time you play, the power of thanos will vary."
print "6.Different skill set of avengers and thanos include their physical strength, intelligence and magical power."
print "7.The final power of avengers is equal to tot_phy_power_avengers+(2*tot_intelligence_avengers)+(0.5*tot_mag_power_avengers)"
print "8.On the other hand, final power of thanos is equal to (1.5*phy_power_thanos)+intelligence_thanos+(2*mag_power_thanos)"
print "9.Different equation for the final power is bcoz of the fact that avengers use more of their intelligence to defeat thanos who is having all the six magical infinity stones with them.{Well, it does make some sense}"
print "10.Finally, their total power is compared and the winner is decided."

play=True
#loop for the entire code for the game
while play:
#creating a master set of all the heroes present in MCU
	heroes=["cap_america","doc_strange","thor","hulk","iron_man","spider_man","black_widow","scarlet_witch","black_panther","hawkeye"]
#getting the name of two heroes from the user
	print "\nEnter any two heroes from the given set only {cap_america,doc_strange,thor,hulk,iron_man,spider_man,black_widow,scarlet_witch,black_panther,hawkeye}:"
	hero1=raw_input("\nenter hero1: ")
	hero2=raw_input("enter hero2: ")
#assinging the other two heroes to make a team of 4
	import random
	hero3=random.choice(heroes)
	hero4=random.choice(heroes)
#making sure that all the team members are different i.e the ramdomly generated heroes differ from the ones entered by the user
	while True:
		if hero1==hero3 or hero2==hero3:
			hero3=random.choice(heroes)
			continue
		else: break

	while True:
		if hero1==hero4 or hero2==hero4 or hero3==hero4:
			hero4=random.choice(heroes)
			continue
		else: break
#displaying the team
	print "\nAvengers Assemble!!!\n"
	print hero1
	print hero2
	print hero3
	print hero4
#assigning tha physical power, intelligence and magical powers to the individual members of the team
	flag1=0
	flag2=0
	flag3=0
	flag4=0
	power1=0
	power2=0
	power3=0
	power4=0
	intelligence1=0
	intelligence2=0
	intelligence3=0
	intelligence4=0
	mag_power1=0
	mag_power2=0
	mag_power3=0
	mag_power4=0
#1
	if hero1=="cap_america" or hero2=="cap_america" or hero3=="cap_america" or hero4=="cap_america":
		power1=90
		intelligence1=98
		mag_power1=0
		flag1=1
#2
	if hero1=="doc_strange" or hero2=="doc_strange" or hero3=="doc_strange" or hero4=="doc_strange":
		if flag1!=1:
			power1=70
			intelligence1=85
			mag_power1=98
			flag1=1
		else:
			power2=70
			intelligence2=85
			mag_power2=98	
			flag2=1
#3
	if hero1=="thor" or hero2=="thor" or hero3=="thor" or hero4=="thor":
		if flag1!=1:
			power1=98
			intelligence1=75
			mag_power1=80
			flag1=1
		elif flag2!=1:
			power2=98
			intelligence2=75
			mag_power2=80
			flag2=1
		else:
			power3=98
			intelligence3=75
			mag_power3=80
			flag3=1
#4
	if hero1=="hulk" or hero2=="hulk" or hero3=="hulk" or hero4=="hulk":
		if flag1!=1:
			power1=95
			intelligence1=55
			mag_power1=0
			flag1=1
		elif flag2!=1:
			power2=95
			intelligence2=55
			mag_power2=0
			flag2=1
		elif flag3!=1:
			power3=95
			intelligence3=55
			mag_power3=0
			flag3=1
		else:
			power4=95
			intelligence4=55
			mag_power4=0
			flag4=1
#5
	if hero1=="iron_man" or hero2=="iron_man" or hero3=="iron_man" or hero4=="iron_man":
		if flag1!=1:
			power1=95
			intelligence1=92
			mag_power1=0
			flag1=1
		elif flag2!=1:
			power2=95
			intelligence2=92
			mag_power2=0
			flag2=1
		elif flag3!=1:
			power3=95
			intelligence3=92
			mag_power3=0
			flag3=1
		elif flag4!=1:
			power4=95
			intelligence4=92
			mag_power4=0
			flag4=1
#6
	if hero1=="spider_man" or hero2=="spider_man" or hero3=="spider_man" or hero4=="spider_man":
		if flag1!=1:
			power1=92
			intelligence1=80
			mag_power1=0
			flag1=1
		elif flag2!=1:
			power2=92
			intelligence2=80
			mag_power2=0
			flag2=1
		elif flag3!=1:
			power3=92
			intelligence3=80
			mag_power3=0
			flag3=1
		elif flag4!=1:
			power4=92
			intelligence4=80
			mag_power4=0
			flag4=1
#7
	if hero1=="black_widow" or hero2=="black_widow" or hero3=="black_widow" or hero4=="black_widow":
		if flag1!=1:
			power1=70
			intelligence1=90
			mag_power1=0
			flag1=1
		elif flag2!=1:
			power2=70
			intelligence2=90
			mag_power2=0
			flag2=1
		elif flag3!=1:
			power3=70
			intelligence3=90
			mag_power3=0
			flag3=1
		elif flag4!=1:
			power4=70
			intelligence4=90
			mag_power4=0
			flag4=1
#8
	if hero1=="scarlet_witch" or hero2=="scarlet_witch" or hero3=="scarlet_witch" or hero4=="scarlet_witch":
		if flag1!=1:
			power1=50
			intelligence1=75
			mag_power1=95
			flag1=1
		elif flag2!=1:
			power2=50
			intelligence2=75
			mag_power2=95
			flag2=1
		elif flag3!=1:
			power3=50
			intelligence3=75
			mag_power3=95
			flag3=1
		elif flag4!=1:
			power4=50
			intelligence4=75
			mag_power4=95
			flag4=1
#9
	if hero1=="black_panther" or hero2=="black_panther" or hero3=="black_panther" or hero4=="black_panther":
		if flag1!=1:
			power1=90
			intelligence1=92
			mag_power1=0
			flag1=1
		elif flag2!=1:
			power2=90
			intelligence2=92
			mag_power2=0
			flag2=1
		elif flag3!=1:
			power3=90
			intelligence3=92
			mag_power3=0
			flag3=1
		elif flag4!=1:
			power4=90
			intelligence4=92
			mag_power4=0
			flag4=1
#10
	if hero1=="hawkeye" or hero2=="hawkeye" or hero3=="hawkeye" or hero4=="hawkeye":
		if flag1!=1:
			power1=75
			intelligence1=85
			mag_power1=0
			flag1=1
		elif flag2!=1:
			power2=75
			intelligence2=85
			mag_power2=0
			flag2=1
		elif flag3!=1:
			power3=75
			intelligence3=85
			mag_power3=0
			flag3=1
		elif flag4!=1:
			power4=75
			intelligence4=85
			mag_power4=0
			flag4=1
#displaying the different skill set of avengers
	print"\nPhysical power of individual avengers (not in order)"
	print "physical power of avenger 1= ",power1
	print "physical power of avenger 2= ",power2
	print "physical power of avenger 3= ",power3
	print "physical power of avenger 4= ",power4
	print"\nIntelligence of individual avengers (again not in order)"
	print "intelligence of avenger 1= ",intelligence1
	print "intelligence of avenger 2= ",intelligence2
	print "intelligence of avenger 3= ",intelligence3
	print "intelligence of avenger 4= ",intelligence4
	print"\nMagical power of individual avengers (again no order)"
	print "magical power of avenger 1= ",mag_power1
	print "magical power of avenger 2= ",mag_power2
	print "magical power of avenger 3= ",mag_power3
	print "magical power of avenger 4= ",mag_power4
#determining the total skill set of the avengers
	tot_phy_power_avengers=power1+power2+power3+power4
	tot_intelligence_avengers=intelligence1+intelligence2+intelligence3+intelligence4
	tot_mag_power_avengers=mag_power1+mag_power2+mag_power3+mag_power4
#displayinmg them
	print "\nCombined physical power of the avengers: ",tot_phy_power_avengers
	print "Combined intelligence of the avengers: ",tot_intelligence_avengers
	print "Combined magical power of the avengers: ",tot_mag_power_avengers
#randomly finding the power of thanos
	phy_power_thanos=random.randint(325,375)
	intelligence_thanos=random.randint(300,355)
	mag_power_thanos=random.randint(0,130)
#displaying them
	print "\nPhysical power of thanos",phy_power_thanos
	print "Intelligence of thanos",intelligence_thanos
	print "Magical power of thanos",mag_power_thanos
#determining the final power of  avengers and thanos using different algorithm for each of them on the basis of their prevalence in MCU
	final_power_avengers=tot_phy_power_avengers+(2*tot_intelligence_avengers)+(0.5*tot_mag_power_avengers)
	final_power_thanos=(1.5*phy_power_thanos)+intelligence_thanos+(2*mag_power_thanos)
#displaying them
	print "\nFinal power of avengers: ",final_power_avengers
	print "Final power of thanos: ",final_power_thanos
#finally, comparing and giving an end to the fight between avengers and thanos
	if final_power_avengers>=final_power_thanos:
		print "\nYess!! Avengers Win!"
		print "They have saved the world from thanos.."
		print "Victory!!"
	else:
		print "\nOh Sh*t! Thanos snaps his finger and destroys half the universe.."
		print "Avengers fail to save the world this time.."
		print "Well! Remember the words from Tony Stark: If we can't save the world, then we are damn sure that we'll avenge it!!"
		print "Avengers will definitely be back to save the world, wait will end on 3rd May 2019.. "
		print "Better luck next time!"
#asking the user if he/she wants to play again
	again=raw_input("Do you want to play again {type yes or no}")
	if again=="no":
		play=False

#this one is just to see the output on screen. Otherwise the output screen just vanishes on my system. Sorry for this. Hope this game works fine..
x=input("\nenter a number: ")
print x
