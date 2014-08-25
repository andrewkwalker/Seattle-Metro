import csv

routeMap = {}
routeMap[1] = ['10th Ave W & W Fulton St', 'Queen Anne Ave N & Mercer St', 
				 '3rd Ave & Cedar St', '3rd Ave & Union St', '5th Ave S & S Jackson St']
routeMap[2] = ['7th Ave W & W Raye St', 'Queen Anne Ave N & Mercer St', 
				 '3rd Ave & Union St', 'Broadway & E Union St', 
				 'Madrona Dr & Lake Washington Blvd']
routeMap[3] = ['1st Ave W & W Raye St', 'Nob Hill Ave N & Galer St', 
			   'Queen Anne Ave N & Boston St', '5th Ave N & Broad St', 
			   '3rd Ave & Union St', 'Broadway & E Jefferson St', 
			   '21st Ave & E Jefferson St', '34th Ave & E Union St', 
			   '25th Ave S & S Walker St']
routeMap[4] = ['1st Ave W & W Raye St', 'Nob Hill Ave N & Galer St', 
			   'Queen Anne Ave N & Boston St', '5th Ave N & Broad St', 
			   '3rd Ave & Union St', 'Broadway & E Jefferson St', 
			   '21st Ave & E Jefferson St', '34th Ave & E Union St', 
			   '25th Ave S & S Walker St']
routeMap[5] = ['Shorline Community College', 'N 145th St & Greenwood N', 
			   'Greenwood Ave N & Holman Rd N', 'N 85th St & Greenwood Ave N',
			   'Phinney Ave N & N 46th St', 'Fremont Aurora Bridge On-Ramp',
			   '5th Ave & Wall St', '3rd Ave & Pike St', '3rd Ave S & S Main St']
routeMap[6] = ['3rd Ave & Pine St', '3rd Ave & Union St', '12th Ave S & S Jackson St',
			   'Rainier Ave S & S Genesee St', 'Rainier Ave S & S Graham St',
			   'Rainier Ave S & S Henderson St', '62nd Ave S & S Prentice St',
			   'S Henderson St & Rainier Ave S']
routeMap[8] = ['S Henderson St & Rainier Ave S', 'Rainier Ave S & S Forest St',
			   '23rd Ave S & S Jackson St', 'ML King Jr Way & E Madison St',
			   'E John St & Broadway Ave E', 'Queen Anne Ave N & Mercer St']
routeMap[9] = ['10th Ave E & E Aloha St', 'Broadway & E Pine St', 
			   '12th Ave S & S Jackson St', 'Rainier Ave S & Walker St', 
			   'Rainier Ave S & S Graham St', 'ML King Jr Way S & S Henderson St']
routeMap[10] = ['15th Ave E & E Galer St', '15th Ave E & E John St', 
				'Broadway Ave & E Pine St', 'Pine St & 9th Ave', 'Pine St & 5th Ave']
routeMap[11] = ['42nd Ave E & E McGilvra St', '23rd Ave E & E Madison St',
				'Broadway & E Pine St', '3rd Ave & Pine St']
routeMap[12] = ['Marion St & 2nd Ave', 'Broadway & E Madison St', '15th Ave & E Madison St',
				'19th Ave E & E Galer St']
routeMap[13] = ['3rd Ave W & W Cermona St', 'Queen Anne Ave N & Mercer St', 
				  '3rd Ave & Union St']
routeMap[14] = ['3rd Ave & Cedar St', '3rd Ave & Union St', '5th Ave s & S Jackson St',
				'23rd Ave S & S Jackson St', 'Rainier Ave S & S Forest St',
				'Mt Baker Dr S & S Hanford St']
routeMap[15] = ['24th Ave NW & NW 85th St', '24th Ave NW & NW 85th St', 'Loyal Ave NW & View Ave NW',
				'14th Ave NW & NW 105th St', '15th Ave NW & NW 85th St', 'Ballard Ave NW & NW Market St',
				'15th Ave NW & NW Market St', 'Denny Way & Warren Pl', '3rd Ave & Pike St', '3rd Ave S & S Main St']
routeMap[16] = ['Transit Center Roadway & NE 103rd St', 'College Way & N 97th St', 'Woodlawn Ave NE & NE Ravenna Blvd',
				'Stone Way N & N 45th St', 'Bridge Way N & N 38th St', '3rd Ave & Union St', 'Alaskan Way & Marion St']
routeMap[17] = ['24th Ave NW & NW 85th St', '24th Ave NW & NW 85th St', 'Loyal Ave NW & View Ave NW',
				'14th Ave NW & NW 105th St', '15th Ave NW & NW 85th St', 'Ballard Ave NW & NW Market St',
				'15th Ave NW & NW Market St', 'Denny Way & Warren Pl', '3rd Ave & Pike St', '3rd Ave S & S Main St']
routeMap[18] = ['24th Ave NW & NW 85th St', '24th Ave NW & NW 85th St', 'Loyal Ave NW & View Ave NW',
				'14th Ave NW & NW 105th St', '15th Ave NW & NW 85th St', 'Ballard Ave NW & NW Market St',
				'15th Ave NW & NW Market St', 'Denny Way & Warren Pl', '3rd Ave & Pike St', '3rd Ave S & S Main St']
routeMap[19] = ['Magnolia Blvd W & W Emerson St', '34th Ave W & W McGraw St', '28th Ave W & W Blaine St', '3rd Ave & Cedar St',
				'3rd Ave & Pike St']
routeMap[21] = ['5th Ave & Wall St', '3rd Ave & Pike St', '3rd Ave & S Main St', '1st Ave S & S Spokane St',
				'35th Ave SW & SW Avalon Way', '35th Ave SW & SW Morgan St', '29th Ave SW & SW Barton St']
routeMap[22] = ['3rd Ave & Pike St', 'California Ave SW & SW Alaska St', '41st Ave SW & SW Thistle St',
				'25th Ave SW & SW Henderson St', '26th Ave SW & SW Roxbury St']
routeMap[24] = ['Magnolia Blvd W & W Emerson St', '34th Ave W & W McGraw St', '28th Ave W & W Blaine St',
				'3rd Ave & Cedar St', '3rd Ave & Pike St']
routeMap[25] = ["Children's Hospital", '55th Ave NE & NE 44th St', 'U of W Campus HUB', 'Montlake Station On Montlake Blvd at SR-520',
				'Boylston Ave E & E Roanoke St', '3rd Ave & Union St', 'S Washington St & 4th Ave S']
routeMap[26] = ['N 143rd St & Linden Ave N', '8th Ave NW & NW 97th St', '8th Ave NW & NW Market St',
				'Woodlawn Ave NE & NE Ravenna Blvd', 'Latona Ave NE & NE 45th St', 'Fremont Ave N & N 34th St',
				'Dexter Ave N & Harrison St', '3rd Ave & Pike St']
routeMap[27] = ['3rd Ave & Cedar St', '3rd Ave & Union St', '3rd Ave & Yesler Way', 'Broadway & E Yesler Way',
				'23rd Ave & E Yesler Way', '36th Ave S & S Atlantic St']
routeMap[28] = ['N 143rd St & Linden Ave N', '8th Ave NW & NW 97th St', '8th Ave NW & NW Market St',
				'Woodlawn Ave NE & NE Ravenna Blvd', 'Latona Ave NE & NE 45th St', 'Fremont Ave N & N 34th St',
				'Dexter Ave N & Harrison St', '3rd Ave & Pike St']
routeMap[29] = ['W Market St & 28th Ave NW', 'NW Market St & Ballard Ave NW', '15th Ave NW & NW Leary Way',
				'3rd Ave W & W Cermona St', 'Queen Anne Ave N & W Galer St', '2nd Ave & Pike St',
				'2nd Ave Ext S & S Jackson St']
routeMap[82] = ['3rd Ave & Pine St', '5th Ave N & Broad St', 'Bridge Way N & N 38th St',
				'1st Ave NE & NE 80th St', '5th Ave N & Mercer St', '3rd Ave & Pine St']
routeMap[83] = ['3rd Ave & Pine St', 'University Way NE & NE 45th St', '15th Ave NE & NE 80th St', '25th Ave NE & NE 65th St',
				'Pine St & 3rd Ave']
routeMap[84] = ['4th Ave S & S Royal Brougham Way', '3rd Ave & Pike St', '23rd Ave & E Union St',
				'42nd & E McGilvra St', '34th Ave & E Union St', 'Pine St & 3rd Ave']
routeMap[99] = ['Alaskan Way & Clay St', 'Yesler Way & Post Ave', '8th Ave S & S King St']
routeMap[60] = ['Broadway & E Republican St', 'Broadway & E Pine St', '9th Ave & Jefferson St', '12th Ave S & S Jackson St', 'Beacon Ave S & S Lander St', 
				'VA Medical Center', '13th Ave S & S Bailey St', '14th Ave S & S Trenton St', '25th Ave SW & SW Henderson St']
routeMap[61] = ['24th Ave NW & NW 85th St', '32nd Ave NW & NW 85th St', 'NW Market St & Ballard Ave NW', 'NW Leary Way & 15th Ave NW', 'NW Ballard Way & 11th Ave NW']
routeMap[62] = ['4th Ave S & S Jackson St', '3rd Ave & Pine St', 'Westlake Ave N & Mercer St', '3rd Ave W & W Nickerson St',
				'Ballard Ave NW & NW Market St', '28th Ave W & NW Market St']
routeMap[64] = ['32nd Ave NE & NE 143rd St', '35th Ave NE & NE 95th St', '35th Ave NE & NE 65th St', 'NE 65th St & 15th Ave NE', 'Stewart St & 9th Ave',
				'5th Ave & Pike St', 'Boren Ave & Madison St', '9th Ave & Jefferson St', '17th Ave & E Jefferson St']
routeMap[65] = ['30th Ave NE & NE 143rd', '35th Ave NE & NE 125th St', '35th Ave NE & NE 65th St', '40th Ave NE & Sand Point Way NE', 'U of W Campus HUB',
				'Brooklyn Ave NE & NE Campus Pkwy', 'Downtown Seattle Tunnel University Street Station Bay C']
routeMap[66] = ['Transit Roadway & NE 103rd St', 'Roosevelt Way NE & NE 75th St', 'Roosevelt Way NE & NE 45th St', 'U of W Campus HUB', '3rd Ave & Union St', 'Alaskan Way & Marion St']
routeMap[67] = ['Transit Roadway & NE 103rd St', 'Roosevelt Way NE & NE 75th St', 'Roosevelt Way NE & NE 45th St', 'U of W Campus HUB', '3rd Ave & Union St', 'Alaskan Way & Marion St']
routeMap[68] = ['NE Campus Pkwy & Brooklyn Ave NE', 'U of W Campus HUB', '25th Ave NE & NE 75th St', 'Roosevelt Way NE & NE 92nd St', 'Transit Center Roadway & NE 103rd St']
routeMap[70] = ['NE 50th St & Brooklyn Ave NE', 'Eastlake Ave E & Harvard Ave E', 'Fairview Ave & Denny Way', '3rd Ave & Union St']
routeMap[71] = ['NE 85th St & 35th Ave NE', 'NE 65th St & 35th Ave NE', 'NE 65th St & 15th Ave NE', 'University Way NE & NE 45th St', 'Fairview Ave N & Denny Way',
				'Downtown Seattle Tunnel University Street Station Bay C', 'Downtown Seattle Tunnel International District Station Bay C', '2nd Ave & Pike St']
routeMap[72] = ['NE 130th St & 35th Ave NE', 'Lake City Way NE & NE 125th St', 'NE 80th St & 15th Ave NE', 'NE 65th St & 15th Ave NE', 'University Way NE & NE 45th St',
				'Fairview Ave N & Denny Way', 'Downtown Seattle Tunnel University Street Station Bay C', 'Downtown Seattle Tunnel International District Station Bay C', '2nd Ave & Pike St']
routeMap[73] = ['NE 136th St & 17th Ave NE', 'NE 125th St & 15th Ave NE', 'NE 80th St & 15th Ave NE', 'NE 65th St & 15th Ave NE', 'University Way NE & NE 45th St', 
				'Fairview Ave N & Denny Way', 'Downtown Seattle Tunnel University Street Station Bay C', 'Downtown Seattle Tunnel International District Station Bay C', '2nd Ave & Pike St']
routeMap[74] = ['Sandpoint NOAA Bldg 3', '63rd Ave NE & NE 74th St', '35th Ave NE & NE 55th St', 'University Way NE & NE 45th St', 'Downtown Seattle Tunnel University Street Station Bay C', 
				'Downtown Seattle Tunnel International District Station Bay C']
routeMap[75] = ['Transit Center Roadway & NE 103rd St', 'Lake City Way NE & NE 125th St', 'NE 74th St & Sand Point Way NE', 'Sand Point Way NE & 40th Ave NE', 'NE Campus Prkwy & Brooklyn Ave NE']
routeMap[76] = ['35th Ave NE & NE 85th St', 'NE 65th St & 35th Ave NE', 'NE 65th St & 15th Ave NE', 'Downtown Seattle Tunnel University Street Station Bay C',
				'Downtown Seattle Tunnel International District Station Bay C']
routeMap[77] = ['NE 175th St & 10th Ave NE', 'NE 125th St & 15th Ave NE', 'NE 80th St & 15th Ave NE', 'Downtown Seattle Tunnel University Street Station Bay C', 
				'Downtown Seattle Tunnel International District Station Bay C']
routeMap[30] = ['NOAA Bldg 3', 'NE 74th St & Sand Point Way NE', 'NE 65th St & Sand Point Way NE', 'NE 55th St & 35th Av NE',
                 'University Way NE & NE 45th St', '12th Ave NE & NE Campus Pkwy', 'Downtown Seattle Tunnel International District Station Bay C']
routeMap[31] = ['Sand Point Way NE & 50th St', '40th Ave NE & NE 50th St', 'U of W Campus HUB', '12th Ave NE & NE Campus Pkwy',
                'Stone Way N & N 40th St', 'Fremont Ave N & N 34th St', '3rd Ave W & W Nickerson St', 'Queen Anne Av N & Harrison St',
                'Condon Way W & W McGraw St']
routeMap[32] = ['Sand Point Way NE & 50th St', '40th Ave NE & NE 50th St', 'U of W Campus HUB', '12th Ave NE & NE Campus Pkwy',
                'Stone Way N & N 40th St', 'Fremont Ave N & N 34th St', '3rd Ave W & W Nickerson St', 'Queen Anne Av N & Harrison St',
                'Condon Way W & W McGraw St']
routeMap[33] = ['Illinois Ave & Texas Way', '34 Ave W & W Government Way', '28th Ave W & W Blaine St', '3rd Ave & Cedar St',
                '3rd Ave & Union St', '3rd Ave & Yesler Way']
routeMap[36] = ['3rd Ave & Pine St', '5th Ave S & S Jackson St',  '12th Ave S & S Jackson St', 'Beacon Ave S & S Lander St'
                'Beacon Ave S & S Columbian Way	Beacon Hill', 'Beacon Ave S & S Myrtle St', '39th Ave S & S Myrtle St']
routeMap[37] = ['35th Ave SW & SW Alaska St', '44th Ave SW & SW Alaska St',  '48th Ave SW & Beach Dr SW', '63rd Ave SW & Alki Ave SW',
                '28th Ave SW & SW Spokane St', '1st Ave S & S Spokane St', '4th Ave S & S Jackson St', '3rd Ave & Pike St']
routeMap[40] = ['Transit Center Roadway & NE 103rd St', 'Aurora Ave N & N 105th St', '24th Ave NW & NW 83rd St', 'Ballard Ave NW & NW Market St'
                'Fremont Ave N & N 34th St', '9th Ave N & Mercer St', '3rd Ave & Union St', '3 Ave S & S Main St']
routeMap[41] = ['NE 130th St & 35th Ave NE', '5th Ave NE & NE 125th St', 'NE 103rd St & Transit Roadway',
                'Dowtown Seattle University Street Station Bay C', 'Downtown Seattle Tunnel International District Station Bay C']
routeMap[43] = ['NE 45th St & University Way NE', 'Montlake Station On Montlake Blvd at SR-520', 'Broadway E & E John St', 'Pine St & 5 Ave']
routeMap[44] = ['NW 54th St & 32nd Ave NW', 'Ballard Ave NW & NW Market St', 'N 46th St & Phinney Ave N', 'N 45th St & Stone Way N',
                'NE 45th & Univeristy Way NE', 'Montlake Blvd NE & NE Pacific Pl', 'Montlake Station On Montlake Blvd at SR-520']
routeMap[47] = ['Bellevue Ave E & Bellevue Pl E', '9th Ave & Pine St', '5th Ave & Pine St']
routeMap[48] = ['32nd Ave NW & Loyal Way NW', 'Greenwood Ave N & N 85th St', 'Woodlawn Park Ave NE & Ravenna Blvd', '15th Ave NE & NE 65th St',
                '15th Ave NE & 45th St', 'Montlake Station on Montlake Blvd at SR-520', '23rd Ave E & E Madison St', '23rd Ave S & S Jackson St',
                'Rainier Ave S & S Forest St']
routeMap[49] = ['12th Ave NE & NE 47th St', 'Eastlake Ave E & Harvard Ave E', 'Broadway & E Roy St', 'Broadway & E Pine St', 'Pine St & 5th Ave']
routeMap[50] = ['ML King Jr Way S & S Othello St', 'Seward Park Ave S & Wilson Ave S', 'Rainier Ave S & S Genesee St', 'Beacon Hill VA Medical Center',
                'SODO Busway & S Lander St', '44 Ave SW & SW Alaska St', '61st Ave SW & Alki Ave SW']
routeMap[55] = ['California Ave SW & SW Atlantic St', 'California Ave SW & SW Admiral Way', 'California Ave SW & SW Alaska St', '35th Ave SW & SW Avalon Way',
                '3rd Ave & Pine St']
routeMap[56] = ['44th Ave SW & SW Oregon St', '55th Ave SW & SW Dakota St', '61st Ave SW & Alki Ave SW', 'California Ave SW & SW Admiral Way',
                'Seneca St & 2nd Ave', '3rd Ave & Pine St']
routeMap[57] = ['44th Ave SW & SW Oregon St', '55th Ave SW & SW Dakota St', '61st Ave SW & Alki Ave SW', 'California Ave SW & SW Admiral Way',
                'Seneca St & 2nd Ave', '3rd Ave & Pine St']

routeNumbers = routeMap.keys()

with open('output.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(['Route #', 'Redundancy'])
	for route in routeNumbers:
		routeNumbers = routeMap.keys()
		maxChain = 0
		routeNumbers.remove(route)
		for other in routeNumbers:
			chain = set(routeMap[route]).intersection(set(routeMap[other]))
			if len(chain) > maxChain:
				maxChain = len(chain)
		writer.writerow([route, maxChain])