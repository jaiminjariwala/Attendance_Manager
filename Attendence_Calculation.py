# Attendance Calculation and Prediction(for how much still slots require to reach the min_attendance_criteria)!

# min_attendance_required = 75% in my college, let's suppose!

required_slots = 0

def attendance_calculation():

    """Taking input for
        1. How many times user want to check the attendance
        2. Minimum Attendance required in User's college
        3. Number of 'Present_Slots'
        4. Total Number of Lectures/Lab(Slots) Done"""

    global required_slots
    while int(input("\n\t\tEnter 0 or 1 to Continue with the input:\n\t\t")) == 0:

        # inputs...
        min_attendance_required = int(input("\t\tEnter the Minimum Attendance Required in your College:\n\t\t"))
        present_slot = int(input("\t\tEnter the Number of your 'Present' Slots:\n\t\t"))        # 6
        total_slot = int(input("\t\tEnter the Total Number of Slots:\n\t\t"))              # 14

        # Attendance calculation Formula function...
        def attendance_calc_formula(present_slot, total_slot):
            Attendance_calc_formula = present_slot / total_slot * 100
            return Attendance_calc_formula

        print("\t\tYour Current Attendance is: ", round(attendance_calc_formula(present_slot, total_slot), 3), "%", "\n")

        """To know How many Slots User need to Attend to reach minimum attendance requirement...
            1. Increasing the numerator and denominator by 1 then...
            2. Getting the attendance_percentage and then...
            3. comparing the attendance_percentage with min_attendance required(every time the loop runsuntil it meets the 
            min_attendance_requirement!)"""

        while True:

            # for testing, let's take... 6 present slots and 14 total slots

            present_slot = present_slot + 1     # 7,8,9,..., 24     # total 18 for testing
            total_slot = total_slot + 1       # 15,16,..., 32

            # counting for how many more slots require, to reach the minimum attendance requirement for your college
            required_slots = required_slots + 1

            # calling attendance_calc_formula function...
            attendance_calc_formula(present_slot, total_slot)

            # Comparing attendance percentage value with min_attendance_Required
            if attendance_calc_formula(present_slot, total_slot) == min_attendance_required:
                print("\t\t***** You Require", required_slots, "Slots more to reach 75% attendance *****\n")
                print("\t\t***** Then Your attendance will be: ", attendance_calc_formula(present_slot, total_slot))
                break
            elif attendance_calc_formula(present_slot-1, total_slot-1) > min_attendance_required:
                print("\t\t***** Chill! You are NOT in Detention List:), You already Have Sufficient Attendance *****\n")

                # to tell user, how much more bunk he/she can do...

                updated_present_slot = present_slot - 1     # 14 - 1 = 13 (original_present_slot)
                updated_total_slot = total_slot - 1         # 15 - 1 = 14 (original_total_slot)
                updated_required_slot = 0

                while True:
                    updated_total_slot = updated_total_slot + 1             # 15, 16, 17, 18
                    updated_required_slot = updated_required_slot + 1       # 1, 2, 3, 4
                    attendance_calc_formula(updated_present_slot, updated_total_slot)
                    # (13,14)->0->92.85, (13,15)->1->86.67, (13,16)->2->81.25, (13,17)->3->76.47, (13,18)->4->72.22

                    if attendance_calc_formula(updated_present_slot, updated_total_slot) <= min_attendance_required:
                        print("\t\t***** You can Bunk", updated_required_slot-1, "lectures")
                        print("\t\t\t  Your Attendance then will be", attendance_calc_formula(updated_present_slot, updated_total_slot-1))
                        print("\t\t\t  Then after you can fall under Detention List *****\n")
                        break
                break
            else:
                continue

# main driver code...
attendance_calculation()

# ----------------------------------------------- OVER ------------------------------------------------------

# num = 0
# formula_array = []
# slot_array = []
# while int(input("Enter 0 or 1 to Continue with the input: ")) == 0:
#     present_slot = num
#     absent_slot = num + 1
#     slot = (present_slot, absent_slot)
#     print("Present_slot: ", present_slot, ", Absent_slot: ", absent_slot)
#     slot_array.append(slot)
#
#     Formula = present_slot / absent_slot * 100
#     formula_array.append(Formula)
#     print("Your Attendence is: ", Formula)
#     num = num + 1
#
# plt.plot(formula_array, slot_array)
# plt.xlabel("Attendence")
# plt.ylabel("Present/Absent Slot")
# plt.legend(['Present_Slot', 'Absent_Slot'])
# plt.xticks(np.arange(0,100,5))
# plt.title("Attendence Ratio Plot")
# plt.grid()
# plt.show()





