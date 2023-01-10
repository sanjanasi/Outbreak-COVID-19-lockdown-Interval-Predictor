from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

def relief(r):
        if r == "Yes":
                def button5():
                        print("Submitting Form...")
                        print("Form Submitted...")
                        if paymentmodevalue.get():
                                pass
                        else:
                                messagebox.showinfo("Empty Field","UPI Field Required For Payment")
                
                        if otpvalue.get():
                                pass
                        else:
                                messagebox.showerror("Empty Field","OTP Field Required For Payment")
                        with open ("records.txt","a") as f:
                                f.write(f"EMERGENCY CONTACT NUMBER IS {Emergencyvalue.get()}, Customer UPI Details {paymentmodevalue.get()} Customer OTP {otpvalue.get()}\n")

                l19 = Label(f4, text='''Provide Details For Payment''', bg="medium aquamarine", font="15")
                l19.grid(row=4,column=0)
                l20 = Label(f4, text=".").grid(row=5,column=0)
        
                paymentmode = Label(f4, text="Enter UPI",bg="linen", 
                font="Times 12 bold", relief=SUNKEN)
                paymentmode.grid(row=6, column=0)
                paymentmodevalue = StringVar()
                paymentmodeentry = Entry(f4, textvariable=paymentmodevalue,bg="azure", 
                font="Times 12 bold", relief=RAISED)
                paymentmodeentry.grid(row=6, column=1)

                l22 = Label(f4, text=".").grid(row=7,column=0)
                Emergency = Label(f4, text="Emergency Contact Number", bg="linen", 
                font="Times 12 bold", relief=SUNKEN)
                Emergency.grid(row=8, column=0)
                Emergencyvalue = IntVar()
                Emergencyentry = Entry(f4, textvariable=Emergencyvalue,bg="azure", 
                font="Times 12 bold", relief=RAISED)
                Emergencyentry.grid(row=8, column=1)

                l24 = Label(f4, text=".").grid(row=9,column=0)
                otp = Label(f4, text="Enter Otp", bg="linen", font="Times 12 bold", 
                relief=SUNKEN).grid(row=10, column=0)
                otpvalue = IntVar()
                otpentry = Entry(f4, textvariable=otpvalue,bg="azure", 
                font="Times 12 bold", relief=RAISED)
                otpentry.grid(row=10, column=1)

                button5 = Button(f4, text="Proceed Payment",fg="blue",bg="blanched almond",
                activeforeground="darkblue", command=button5, font="Times 15 bold")
                button5.grid(row=11, column=1)
        if r == "No":
                l16 = Label(f4, text='''Thans For Your Concern\n Have a Good Day\n
                Bye Bye!''', bg ="medium aquamarine", fg="black",font="Times 25 bold")
                l16.grid(row=4,column=0)

def predictor(s):
        if s =="Relief Fund":
                u = StringVar(f4)
                u.set("Would U Like To Contribute to\nCovid Relief Fund")
                options1 = OptionMenu(f4,u,"Yes","No",command=relief)
                options1.grid(row=2,column=1)
                options1.config(fg="honeydew2",bg="light sea green",font="Times 13", 
                activeforeground="darkblue",activebackground='aquamarine')
                options1["menu"].config(bg="lemon chiffon",fg="blue",font="Times 13 bold")

        if s =="Lockdown Predictor":
                def proceed():
                        if casevalue.get():
                                if casevalue.get()>=200000:
                                        l96 = Label(f4, text=f"LockDown is mandatory \nand required in your country. ", 
                                        fg="black", bg='slate gray', font="Times 17 bold", relief=RAISED)
                                        l96.grid(row=4,column=0)
                                else:
                                        l95 = Label(f4, text=" Your country  is out of danger.\nNo lockdown Required  ",
                                        fg="black", bg='slate gray', font="Times 17 bold", relief=RAISED)
                                        l95.grid(row=4,column=0)
                        else:
                                messagebox.showinfo("Warning","Cases Are mandatory")
                        
                        if countryvalue.get():
                                pass                

                        print("Submitting Form...")
                        print("Form Submitted...")
                        with open ("records.txt","a") as f:
                                f.write(f"User's Country of reident {countryvalue.get()}, cases {casevalue.get()}\n")
       
                l100 = Label(f4, text=" Enter Country Name : ", fg="black", bg='slate gray', 
                font="Times 14 bold", relief=RAISED).grid(row=1,column=0)

                countryvalue = StringVar()
                e100 = Entry(f4, textvariable=countryvalue, bg='linen', font="Times 13 bold", 
                relief=SUNKEN).grid(row=1, column=1)

                l99 = Label(f4, text=" Total Active Cases : ", fg="black", bg='slate gray', 
                font="Times 14 bold", relief=RAISED)
                l99.grid(row=2,column=0)

                casevalue = IntVar()
                e99 = Entry(f4, textvariable=casevalue, bg='linen', font="Times 12 bold", 
                relief=SUNKEN).grid(row=2, column=1)

                l98 = Label(f4, text=webbrowser.open("https://www.worldometers.info/coronavirus/#countries"))
                l98.grid(row=3,column=1)

                button5 = Button(f4 ,text="Proceed",fg="honeydew2",bg="light sea green",
                activeforeground="darkblue", command=proceed, font="Times 12 bold")
                button5.grid(row=3, column=2)

        
def a_c():
        second = Tk(className="About_Covid")
        second.geometry("1360x720+0+0")
        second.resizable(True,True)
        second.minsize(400,300)
        second.maxsize(2160,1080)
        second.attributes('-fullscreen',False)
        
        f7 = Frame(second, relief=RAISED)
        f7.grid(row=0,column=0)

        l7 = Label(f7, text='''The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing global pandemic 
        of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The novel 
        virus was first identified in the Chinese city of Wuhan in December 2019; a lockdown in Wuhan and other cities in 
        surrounding Hubei failed to contain the outbreak, and it quickly spread to other parts of mainland China and around the 
        world. The World Health Organization (WHO) declared a Public Health Emergency of International Concern on 30 January 2020, 
        and a pandemic on 11 March 2020. Multiple variants of the virus have emerged and become dominant in many countries since 2021, 
        with the Alpha, Beta, Gamma and Delta variants being the most virulent. As of 20 November 2021, more than 256 million cases and 
        5.14 million deaths have been confirmed, making the pandemic one of the deadliest in history.COVID-19 symptoms range from none to 
        life-threatening. Severe illness is more likely in elderly patients and those with certain underlying medical conditions. Transmission 
        of COVID-19 occurs when people breathe in air contaminated by droplets and small airborne particles. The risk of breathing these in is 
        highest when people are in close proximity, but the virus can transmit over longer distances, particularly indoors and in poorly ventilated 
        areas. Transmission can also occur, rarely, via contaminated surfaces or fluids. People remain contagious for up to 20 days, and can spread 
        the virus even if they do not develop symptoms.\nNAMING\nThe pandemic is known by several names. It is often referred to as its colloquial name, 
        "the coronavirus pandemic", despite the existence of other human coronaviruses that have caused epidemics and outbreaks (e.g. SARS). Before it 
        was declared a pandemic, it was known as "the coronavirus outbreak" and "Wuhan coronavirus outbreak\nBakcground\nAlthough the exact origin of 
        the virus is still unknown, the first outbreak started in Wuhan, Hubei, China, in November 2019. Many early cases of COVID-19 were linked to people 
        who had visited the Huanan Seafood Wholesale Market in Wuhan, but it is possible that human-to-human transmission was already happening before this. 
        On 11 February 2020, the World Health Organization (WHO) named the disease "COVID-19", which is short for "coronavirus disease 2019".The virus that 
        caused the outbreak is known as severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), a newly discovered virus closely related to bat coronaviruses, 
        pangolin coronaviruses, and SARS-CoV.[33] The scientific consensus is that the virus is most likely of zoonotic origin, from bats or another closely-related 
        mammal.Despite this, the subject has generated extensive speculation and conspiracy theories,which were amplified by rapidly growing online echo chambers. 
        Global geopolitical divisions, notably between the United States and China, have been heightened because of this issue.''', font="Times 13 bold", 
        bg="misty rose").grid(row=0,column=0)

        second.mainloop()

def c_l_s():
        third = Tk(className="Covid_Live_Status")
        third.geometry("1360x720+0+0")
        third.resizable(True,True)
        third.minsize(400,300)
        third.maxsize(2160,1080)
        third.attributes('-fullscreen',False)
        
        f9 = Frame(third, relief=RAISED)
        f9.grid(row=0,column=0)
        f10 = Frame(third, relief=RAISED)
        f10.grid(row=1,column=0)
       
        l9 = Label(f9, webbrowser.open("https://www.worldometers.info/coronavirus/"))
        l9.grid(row=0,column=0)
        
        image08 = Image.open("08.jpg")
        photo6 = ImageTk.PhotoImage(image08)
        l10 = Label(f10, image=photo6)
        l10.grid(row=0,column=0)

        third.mainloop()

def l_h_i():
        fourth = Tk(className="Lockdown History of India")
        fourth.geometry("1360x720+0+0")
        fourth.resizable(True,True)
        fourth.minsize(400,300)
        fourth.maxsize(2160,1080)
        fourth.attributes('-fullscreen',False)
        
        f11 = Frame(fourth, relief=RAISED)
        f11.grid(row=0,column=0)
       
        l10 = Label(f11, text='''On the evening of 24 March 2020, the Government of India under Prime Minister Narendra Modi ordered a nationwide lockdown for 21 days, limiting movement of the entire 
        1.38 billion (138 crore) population of India as a preventive measure against the COVID-19 pandemic in India. It was ordered after a 14-hour voluntary public curfew on 22 March, followed by 
        enforcement of a series of regulations in the countries' COVID-19 affected regions \nPhase 1 (24 March – 14 April)\nOn 24 March, the first day of the lockdown, nearly all services and factories 
        were suspended.People were hurrying to stock essentials in some parts. Arrests across the states were made for violating norms of lockdown such as venturing out for no emergency, opening businesses 
        and also home quarantine violations. The government held meetings with e-commerce websites and vendors to ensure a seamless supply of essential goods across the nation during the lockdown period. 
        Several states announced relief funds for the poor and affected people while the central government was finalising a stimulus package. On 26 March, finance minister Nirmala Sitharaman announced 
        a ₹170,000 crore (US$23 billion) stimulus package to help those affected by the lockdown. The package was aimed to provide food security measures for poor households through direct cash transfers, 
        free cereal and cooking gas for three months.[50] It also provided insurance coverage for medical personnel. On 27 March, the Reserve Bank of India announced a slew of measures to help mitigate the 
        economic impacts of the lockdown. Prior to the announcement of the nationwide lockdown, on 22 March, the government had announced that the Indian Railways would suspend passenger operations through 
        31 March.[citation needed] The national rail network has maintained its freight operations during the lockdown, to transport essential goods. On 29 March, the Indian Railways announced that it would 
        start services for special parcel trains to transport essential goods, in addition to the regular freight service. The national rail operator also announced plans to convert coaches into isolation 
        wards for patients of COVID-19. This has been described as the first time in 167 years that India's rail network had been suspended,[55] although there was also a strike in 1974. Lamp lighting 
        observed on 5 April 2020 during lockdown On 5 April, citizens all over India cheered and showed solidarity with the health workers, police, and all those fighting the disease by switching off 
        the electric lights at home for 9 minutes from 9:00 p.m. to 9:09 p.m. and observed lighting diya, candle; and flashing torchlight and mobile flashlight. As the end of the initial lockdown period 
        came near, many state governments expressed their decision to extend it till the end of April. Among them were Odisha,[59] Punjab, Maharashtra, Karnataka with some relaxations, West Bengal and 
        Telangana. Towards the end of the initial period, the rate of growth of COVID infections in India had significantly slowed, from a rate of doubling every three days before the lockdown to one of 
        doubling every eight days on 18 April.\nPhase 2 (15 April – 3 May)\nOn 14 April, PM Modi extended the nationwide lockdown till 5 May, with a conditional relaxation promised after 20 April for the 
        regions where the spread had been contained by then.[11] He said that every town, every police station area and every state would be carefully evaluated to see if it had contained the spread. 
        The areas that were able to do so would be released from the lockdown on 20 April. If any new cases emerged in those areas, lockdown could be reimposed.On 16 April, lockdown areas were classified 
        as "red zone", indicating the presence of infection hotspots, "orange zone" indicating some infection, and "green zone" with no infections.The government also announced certain relaxations from 
        20 April, allowing agricultural businesses, including dairy, aquaculture, and plantations, as well as shops selling farming supplies, to open. Public works programmes were also allowed to reopen with 
        instructions to maintain social distancing. Cargo vehicles, including trucks, trains, and planes, would run. Banks and government centres distributing benefits would open as well. On 25 April, small 
        retail shops were allowed to open with half the staff. Again social distancing norms were to be followed.On 29 April, The Ministry of Home Affairs issued guidelines for the states to allow 
        inter-state movement of the stranded persons. States have been asked to designate nodal authorities and form protocols to receive and send such persons. States have also been asked to screen the people, 
        quarantine them, and do periodic health checkups.\nPhase 3 (4–17 May)\n On 1 May, the Ministry of Home Affairs (MHA) and the Government of India (GoI) further extended the lockdown period to two weeks 
        beyond 4 May, with some relaxations.[67][68] The country has been split into 3 zones: red zones (130 districts), orange zones (284 districts), and green zones (320 districts).[69] Red zones are those 
        with high coronavirus cases and a high doubling rateorange zones are those with comparatively fewer cases than red zone and green zones are those without any cases in the past 21 days.Normal movement is 
        permitted in green zones with buses limited to 50 percent capacity. Orange zones would allow only private and hired vehicles but no public transportation. The red zones would remain under lockdown. 
        The zone classification would be revised once a week.\n\nPhase 4 (18–31 May)\nOn 17 May, the National Disaster Management Authority (NDMA) and the Ministry of Home Affairs (MHA) extended the lockdown 
        for a period for two weeks beyond 18 May, with additional relaxations. Unlike the previous extensions, states were given a larger sayin the demarcation of Green, Orange and Red zones and the 
        implementation roadmap. Red zones were further divided into to containment and buffer zones. The local bodies were given the authority to demarcate containment and buffer zone.\nUnlock. 
        Unlock 1.0 (1–30 June)\nThe MHA issued fresh guidelines for June, stating that the phases of reopening would "have an economic focus". Lockdown restrictions were only to be imposed in containment zones,
        while activities were permitted in other zones in a phased manner.This first phase of reopening was termed "Unlock 1.0" and permitted shopping malls, religious places, hotels, and restaurants to reopen  
        from 8 June. Large gatherings were still banned, but there were no restrictions on interstate travel.Night curfews were in effect from 9 p.m. to 5 a.m. in all areas and state governments were allowed 
        to impose suitablerestrictions on all activities. In future phases of reopening, further activities are to be permitted. In Phase II, all educational institutions are scheduled to reopen in July, pending 
        consultations with state governments. In Phase III, easing of restrictions on international air travel operation of metros, and recreational activities (swimming pools, gymnasiums, theatres, entertainment 
        parks, bars, auditoriums, and assembly halls) would be decided upon in August.\nUnlock 2.0 (1–31 July)\n Phase II of Unlock began on 1 July under the guidelines and instructions of the MHA and the NDMA.
        Lockdown measures were only imposed in containment zones. In all other areas, most activities were permitted. Night curfews were in effect from 0 p.m. to 5 a.m. in all areas. State governments were allowed
        to put suitable restrictions on all activities, but state borders remained open to all. Inter- and intrastate travel was permitted. Limited international travel was permitted as part of the Vande Bharat Mission.
        Shops were permitted to allow more than five persons at a time. Educational institutions, me recreational activities remained closed till 31 July. Only essential activities were permitted in containment zones whil 
        maintaining strict parameter control and "intensive contact tracing, house-to-house surveillance, and other clinical interventions". Further guidelines regarding usage of Aarogya Setu and masks were reiterated 
        \nUnlock 3.0 (1–31 August)\n Unlock 3.0 for August 2020 removed night curfews and permitted gymnasiums and yoga centres to reopen from 5 August. Educational institutions would remain closed till 31 August. All 
        inter-and intrastate travel and transportation are permitted. Independence Day celebrations are permitted with social distancing.[17] Maharashtra and Tamil Nadu imposed a lockdown for the whole month, while West Bengal 
        imposed lockdowns twice a week. \nUnlock 4.0 (1–30 September)\n On 29 August 2020, the Ministry of Home Affairs issued guidelines for activities permitted in Unlock 4.0. It said that "Lockdown shall remain in force in 
        the Containment Zones till 30th September 2020".[77] Outside the containment zone, however, some activities were given permission. Metro Rail was allowed to be reopened in a graded manner from 7 September. Marriage 
        functions with gatherings of up to 50 people and funereal/last rites ceremonies with up to 20 people were permitted. Religious, entertainment, political, sports, academic functions and gatherings of up to 100 people were 
        allowed. Face coverings/masks were made compulsory in public places, workplaces and during transport \nUnlock 5.0 (1–31 October)\n On 30 September 2020, the Ministry of Home Affairs issued guidelines for activities permitted 
        in Unlock 5.0.[78] For schools it has a preference for online learning if possible, but States and Union Territories will be able to make those decisions from 15 October, in a graded manner. Lockdown shall remain in force 
        strictly in the Containment Zones till 30 November 2020. Also, swimming pools being used for training of sportsperson would be allowed to open. Cinema halls, that had remained close all this while, could finally be opened from 
        15 October 2020, with a 50 percent of their seating capacity. On 3 November the Government of Kerala opened its tourism sector by reopening hill stations, beaches, national park, and inter-state public transport movemen The 
        Government Of India has decided to open all educational institutions by January 2021 including schools and colleges and universities across India. The Government of Kerala has decided to open its school from December 2020 
        \nUnlock 6.0 (1–30 November)\n On 27 October 2020, the Ministry of Home Affairs issued guidelines for activities permitted in Unlock 6.0.[80][81][82] The Ministry of Home Affairs did not make any new changes to the existing  
        Unlock 5.0 guidelines in its latest instructions for another set of unlocking and said that they would continue to be implemented in the month of November too. Also, a handful of states have allowed opening up of more 
        activities outside containment zones and announced partial reopening of schools. Lockdown has been enforced time and again in spite of attempts to permanently move towards an unlock phase.[85] The government of India has 
        extended the ban on scheduled international flights till January 31. Lockdown in 2020 This section needs expansion. You can help by adding to it. (July 2021) In February end 2021, India got hit by the largest COVID wave. 
        It is cited that people started becoming careless, not wearing masks and not following social distancing, around November- April. This wave caused a rapid surge in cases and deaths. Cases started to rise by March 2021, 
        resulting in state-wide lockdowns. In Maharashtra there were total 4 phases of lockdowns from April to June April 5- 15 June 2021 (Lockdown Phase) When cases rapidly increased in Maharashtra, CM Uddhav warned people on 
        March 28, 2021 to imposed complete lockdown and night curfew was imposed. Schools and offices remained shut. On 4 April 2021 Maharashtra CM Uddhav Thackeray announced a lockdown till April 30. On 5 April 2021 everything 
        began to close due to rise in COVID-19 second wave. Only online deliveries were free at this stage. Films like Sooryavanshi, Bunty Babli 2 got postphoned due to COVID-19's 2nd Wave Several States And UTs Like Tamil Nadu, 
        Karnataka, Kerala, Rajasthan, Bihar, NCT Of Delhi, Madhya Pradesh, Uttar Pradesh, Haryana, Odisha, Jharkhand, Chhattisgarh, J&K, Ladakh, Goa, Mizoram, Meghalaya, West Bengal, Uttarakhand, Puducherry, Telangana, Sikkim and 
        Himachal Pradesh imposed complete Lockdown whereas some like Punjab, Chandigarh, Gujarat, Andhra Pradesh, Assam, Arunachal Pradesh and Nagaland Imposed Partial Lockdown and Major Restrictions From 15 June 2021 , 
        Many States started lifting lockdowns and restrictions and moved in Unlock phase \nImpact\n Food delivery services were banned by several state governments despite the central government's approval. Thousands of people 
        emigrated out of major Indian cities, as they became jobless after the lockdown. Following the lockdown, India's electricity demand fell down to a five-month low on 28 March 2020.[89] Many states were keen on opening up 
        liquor shops during the lockdown which was finally allowed in the 3rd phase beginning on 4 May. Reports of a surge in illicit liquor sales and most importantly, drying up of revenue from liquor sales was the main 
        stimulation Due to the lockdown, more than 350 deaths were reported as of 10 May, with reasons ranging from starvation, suicides, exhaustion, road and rail accidents, police brutality and denial of timely medical care. 
        Among the reported deaths, most were among the marginalised migrants and labourers''', 
         font="Times 8 bold", bg="lavender blush", fg="black")
        l10.grid(row=0,column=0)

        fourth.mainloop()

def l_h_w():
        fifth = Tk(className="Lockdown History of World")
        fifth.geometry("1360x720+0+0")
        fifth.resizable(True,True)
        fifth.minsize(400,300)
        fifth.maxsize(2160,1080)
        fifth.attributes('-fullscreen',False)
        
        f13 = Frame(fifth, relief=RAISED)
        f13.grid(row=0,column=0)
       
        l12 = Label(f13, text='''A lockdown can also be used to protect people inside a facility or, for example, a computing system, from a threat or 
        other external event. In buildings doors leading outside are usually locked so that no person may enter or exit. A full lockdown usually means 
        that people must stay where they are and may not enter or exit a building or rooms within it, needing to go to the nearest place designated safe 
        if not already in such a place. The first lockdown was implemented as a preventive measure in response to COVID-19 in Wuhan in January 2020. 
        Procedures for using both emergency and preventive lockdowns must be planned. \nPreventive action\n A preventive lockdown is a preemptive action 
        plan implemented to address an unusual scenario or a weakness in system to preempt any danger to ensure the safety and security of people, 
        organisation and system. The focus for preventive actions is to avoid dangers and risks arising from the nonconformity to the normal circumstances, 
        but also commonly includes improvements in efficiency. Preventive lockdowns are preemptive lockdowns to mitigate risk. Most organisations plan for 
        the emergency lockdowns but fail to plan for other situations that might quickly degrade to dangerous levels. These protocols must be based on the 
        type of threat, and should be kept simple and short for quick learning and implementation, and flexible enough to handle several scenarios. This 
        allows administrators more options to choose from which are easier to use in various scenarios. For example, in case of a loud scene by a parent or 
        an unarmed petty thief being chased by the police through the school playground, this flexible procedure allows school administrators the flexibility 
        to implement a more limited lockdown while teaching in school continues, thus eliminating need for complete emergency lockdown, disruption and delays 
        in resumption of teaching, etc. The consequences of not having procedures to implement such lockdowns is that the situation might quickly escalate 
        where there could be loss of human lives.\nEmergency lockdown\n Emergency lockdowns are implemented when there is imminent threat to the lives or 
        risk of injury to humans, for example, a school's emergency lockdown procedures must be kept short and simple to make them easier to use under real 
        life crisis conditions. Simple procedures can be easily taught with periodic lockdown drills instead of lengthy training. \nIn epidemics and pandemics\n 
        Police conversing with people during a lockdown in Benidorm, Spain \nStay-at-home order\n Lockdowns can limit movements or activities in a community while 
        allowing most organizations to function normally, or limit movements or activities such that only organizations supplying basic needs and services can 
        function normally.\nswine flu pandemic\n A lockdown was implemented in Mexico from April 30 to May 5, 2009 in response to the 2009 swine flu pandemic. \nCOVID-19 lockdowns\n 
        During the COVID-19 pandemic, the term lockdown was used for actions related to mass quarantines or stay-at-home orders.[6] The first lockdown during 
        the pandemic was implemented in Wuhan on January 23, 2020. By early April 2020, 3.9 billion people worldwide were under some form of lockdown—more than 
        half the world's population. By late April, around 300 million people were under lockdown in nations of Europe, while around 200 million people were under 
        lockdown in Latin America.[9] Nearly 300 million people, or about 90 per cent of the population, were under some form of lockdown in the United States, 
        and 1.3 billion people have been under lockdown in India. The lockdown in the Philippines started on 14 March 2020 and is one of the longest and strictest 
        lockdowns with varying levels of community quarantine being imposed on all major islands and cities. Similarly the lockdown in South Africa started on 
        27 March 2020 and progressed through various levels. It is also one of the strictest lockdowns in the world with cigarettes and alcohol banned throughout. 
        [00:40, 22/11/2021] Backup: 3. History events - In the wake of the September 11 attacks (2001), a three-day lockdown of American civilian airspace was initiated.
        At the University of British Columbia (UBC) on January 30, 2008, an unknown threat was made, and the Royal Canadian Mounted Police (RCMP) issued a lockdown order 
        on one of the buildings on campus for six hours, cordoning off the area. A campus alert was sent via email to everyone affiliated with UBC, while those in the 
        building remained locked in it. On April 10, 2008, two Canadian secondary schools were locked down due to suspected firearm threats. George S. Henry Academy 
        was locked down in Toronto, Ontario at approximately 2:00 p.m. The Emergency Task Force (TPS) were contacted and the lockdown lasted for more than two hours.
         New Westminster Secondary School was locked down in New Westminster, British Columbia at approximately 1:40 p.m. The Emergency Response Team (ERT) was called, 
         and the school was under lockdown until 4:30 p.m. Due to the size of the school some students were not able to leave until 7:00 p.m. On April 19, 2013, the entire 
         city of Boston, US was locked down and all public transportation stopped during the manhunt for terrorists Dzhokhar and Tamerlan Tsarnaev, the perpetrators of the 
         Boston Marathon bombing, while the town of Watertown was under heavily armed police and SWAT surveillance, and systematic house-to-house searches were carried out. 
         In Belgium, its capital Brussels was locked down in 2015 for days while security services sought suspects involved with the November 2015 Paris attacks. Later in 2015,
          a terror threat caused the 2015 Los Angeles Unified School District closure.\n In August 2019, the Indian government imposed a lockdown on Jammu and Kashmir after 
          the revocation of the special status of the state, by communications and media blackout, claiming that the lockdown was to curb terrorism. According to Merriam-Webster, 
          the first known use of lockdown occurred in 1973, referring to the confinement of prisoners. Tracking usage changes through events reported up to 1999 in The New York Times:\n
          Feb 12, 1974, Violent Inmates Are Isolated at San Quentin contains the first reference to lockdown.\nJul 29, 1998, Children in Tow, Tourists Stream to Capitol to 
          Mourn Its Guardians, By Lizette Alvarez: "Friday's act by a gunman prompted few calls for a lockdown of the Capitol." \nOct 25, 1998, Report Card in Yonkers On New Schools 
          Chief, By Elsa Brenner: "Dr. Hornsby declared a lockdown in the city's high schools, informing 6,000 students that they could no longer ventue off campus for pizzas and Chinese food."
          \nNov 8, 1998, No More Rotten Odors, Sewage Protesters Say, By David Koeppel: "At Seaford Harbor School, Principal Barbara Bauer, who attended the rally, acknowledged that the smells 
          had resulted in one 'lockdown' in the past year. On Oct. 26, parents say, a lockdown was declared at another school, Mandalay elementary. \nFeb 10, 1999, As Senate Goes Into 
          Lockdown, Quiet Fills Capitol, By Frances X. Clines: "the Senate went into lockdown with President Clinton's fate in its hands.\n"Jun 6, 1999, In Brief: School Hot Line: "there 
          has also been 'a massive security lockdown' at all Yonkers schools. ...All but one entrance door in each school is locked, and safety officers are stationed at each. Everyone entering 
          school buildings is being scanned for weapons.\n"Aug 13, 1999, Schools in New York Area Reassess Safety for Students, By Randal C. Archibold: "The shootings at Columbine High School in 
          Littleton, Colo., have led school officials in the New York City metropolitan area to reassess security and in some cases to make changes to minimize threats. At one extreme is
           West Hartford, Conn., where administrators devised what they termed a 'lockdown' drill in which students and teachers, practicing in case there should be a shooting, lock all doors 
           and stay put until they are told that the police have arrived.'''
           ,bg="lavender blush", fg="black",font="Times 8 bold")
        l12.grid(row=1,column=1)

        fifth.mainloop()

def menu1():
        mymenu = Menu(f1)
        mymenu.add_command(label="about covid", command=a_c)
        mymenu.add_command(label="Covid_Live_Status", command=c_l_s)
        mymenu.add_command(label="Lockdown History Of India", command=l_h_i)
        mymenu.add_command(label="Lockdown History Of World", command=l_h_w)
        mymenu.add_command(label="Covid Lockdown Predictor", command=predictor)
        ws.configure(menu=mymenu)

def button1():
        if(v1.get()):
                v = ""
                if(v1.get()==1):
                        v =" Male"
                elif(v1.get()==2):
                        v =" Female"
                elif(v1.get()==3):
                        v =" others"
                else:
                        messagebox.showerror("NO selction","Please select gender")
        
        if namevalue.get():
                pass
        else:
                        messagebox.showerror("Empty Field","Name Field is Required")
        
        if Agevalue.get():
                pass
        else:
                        messagebox.showerror("Empty Field","Age Field is Required")
        
        if v1.get():
                pass
        else:
                        messagebox.showerror("Empty Field","Gender Field is Required")
        
        print("Submitting Form...")
        print("Form Submitted...")
        with open ("records.txt","a") as f:
                f.write(f"Name is {namevalue.get()}, Age is {Agevalue.get()}, Contact Number is {Phonevalue.get()}, Gender is {v}\n")
        
        if Agevalue.get() >= 15:
                menu1()

#Defining Screen
ws = Tk(className="Covid Prediction Online")
ws.geometry("1360x720+0+0")
ws.resizable(True,True)
ws.minsize(400,300)
ws.maxsize(2160,1080)
ws.attributes('-fullscreen',False)

#Creating Frames
f1 = Frame(ws, relief=RAISED)
f1.grid(row=0,column=1)
f2 = Frame(ws, relief=RAISED)
f2.grid(row=0,column=2)
f3 = Frame(ws, relief=RAISED)
f3.grid(row=1,column=1)
f4 = Frame(ws, relief=RAISED)
f4.grid(row=1,column=2)

#Frame1 Objects
l41 = Label(f1).grid(row=0,column=0)
image06 = Image.open("06.jpg")
photo4 = ImageTk.PhotoImage(image06)
l6 = Label(f1, image=photo4).grid(row=0,column=1)
l32 = Label(f1).grid(row=2,column=1)

l1 = Label(f1, text="Login_Screen", fg="blue", bg='alice blue', 
 font="Times 40 bold", relief=RAISED)
l1.grid(row=0,column=4)

#Frame2 Objects
l36 = Label(f2).grid(row=0,column=0)
l40 = Label(f2).grid(row=0,column=1)
l39 = Label(f2, text="Covid 19..\nPandemic..", fg="black", bg='slate gray', 
 font="Times 25 bold", relief=RAISED).grid(row=0,column=5)

l37 = Label(f2).grid(row=0,column=3)
image15 = Image.open("15.jpg")
photo13 = ImageTk.PhotoImage(image15)
l3 = Label(f2, image=photo13).grid(row=0,column=4)
l31 = Label(f2).grid(row=0,column=2)

image04 = Image.open("05.jpg")
photo2 = ImageTk.PhotoImage(image04)
l4 = Label(f2, image=photo2).grid(row=0,column=7)

#Frame3 Objects
l2 = Label(f3, text="This is 14+ Usable Platform\nSo kindly fill Details to proceed",
 fg="blue", bg="blanched almond", font="Times 17 bold", relief=RAISED)
l2.grid(row=0,column=0)

name = Label(f3, text="Name", bg='linen', font="Times 14 bold", 
 relief=SUNKEN)
name.grid(row=3, column=0)
namevalue = StringVar()
nameentry = Entry(f3, textvariable=namevalue, bg="azure", 
font="Times 14 bold", relief=RAISED)
nameentry.grid(row=4, column=0)
l28 = Label(f3).grid(row=5,column=0)

Age = Label(f3, text="Age", bg="linen", font="Times 14 bold", 
 relief=SUNKEN)
Age.grid(row=6, column=0)
Agevalue = IntVar()
Ageentry = Entry(f3, textvariable=Agevalue, bg="azure", 
 font="Times 13 bold", relief=RAISED)
Ageentry.grid(row=7, column=0)
l29 = Label(f3).grid(row=8,column=0)

Phone = Label(f3, text="Phone",bg="linen",font="Times 14 bold", 
 relief=SUNKEN)
Phone.grid(row=9, column=0)
Phonevalue = IntVar()
Phoneentry = Entry(f3, textvariable=Phonevalue, bg="azure", 
 font="Times 13 bold", relief=RAISED)
Phoneentry.grid(row=10, column=0)

l38 = Label(f3).grid(row=10,column=0)
image03 = Image.open("03.jpg")
photo1 = ImageTk.PhotoImage(image03)
l4 = Label(f3, image=photo1).grid(row=1,column=1)

l30 = Label(f3).grid(row=11,column=0)
button1 = Button(f3, text="Submit Details",fg="blue",bg="blanched almond",activeforeground="darkblue",
 command=button1, font="Times 14 bold").grid(row=12, column=1)

l1=Label(f3, text="Select gender", bg="linen", font="Times 14 bold", 
 relief=SUNKEN)
l1.grid(row=5,column=2)
l34 = Label(f3).grid(row=6,column=2)
v1=IntVar()
g1=Radiobutton(f3,text="Male", bg='lemon chiffon', variable=v1, value=1, 
 font="Times 13 bold", relief=SUNKEN)
g1.grid(row=7, column=2)
g2=Radiobutton(f3,text="FeMale", bg='lemon chiffon', variable=v1, value=2, 
 font="Times 13 bold", relief=SUNKEN)
g2.grid(row=8, column=2)
g3=Radiobutton(f3,text="Other",bg='lemon chiffon', variable=v1, value=3, 
 font="Times 13 bold", relief=SUNKEN )
g3.grid(row=9, column=2)

#Fram4 Objects
image05 = Image.open("04.jpg")
photo3 = ImageTk.PhotoImage(image05)
l5 = Label(f4, image=photo3).grid(row=0,column=0)

v = StringVar(f4)
v.set("Choose From Options")
options = OptionMenu(f4,v,"Relief Fund","Lockdown Predictor",command=predictor)
options.grid(row=0,column=1)
options.config(fg="honeydew2",bg="light sea green",font="Times 15", 
activeforeground="darkblue",activebackground='aquamarine')
options["menu"].config(bg="lemon chiffon",fg="blue",font="Times 15 bold")

ws.mainloop()