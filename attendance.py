# Attendance Calculation and Prediction(for how much still slots require to reach the min_attendance_criteria)!

# min_attendance_required = 75% in my college, let's suppose!

required_slots = 0


def attendance_calculation(*args, **kwargs):
    """Taking input for
        1. How many times user want to check the attendance
        2. Minimum Attendance required in User's college
        3. Number of 'Present_Slots'
        4. Total Number of Lectures/Lab(Slots) Done"""

    global required_slots

        # inputs...

    attendanceElement = Element('attendancePercent')
    presentSlotsElement = Element('presentSlots')
    totalSlotsElement = Element('totalSlots')
    min_attendance_required = int(attendanceElement.value)
    present_slot = int(presentSlotsElement.value)  # 6
    total_slot = int(totalSlotsElement.value)  # 14

    # Attendance calculation Formula function...

    def attendance_calc_formula(present_slot, total_slot):
        Attendance_calc_formula = present_slot / total_slot * 100
        return Attendance_calc_formula

    op1 = Element('output1')
    op2 = Element('output2')
    # op3 = Element('output3')
    
    op1.write (f"Your Current Attendance is: {round(attendance_calc_formula(present_slot, total_slot), 3)} % \n")

    
    while True:

        # for testing, let's take... 6 present slots and 14 total slots

        present_slot = present_slot + 1  # 7,8,9,..., 24     # total 18 for testing
        total_slot = total_slot + 1  # 15,16,..., 32

        # counting for how many more slots require, to reach the minimum attendance requirement for your college

        required_slots = required_slots + 1
        # op3.write(f"For Increasing slots_function right now required slots is {required_slots} <br>")     # wrote for debugging purpose!

        # calling attendance_calc_formula function...

        attendance_calc_formula(present_slot, total_slot)

        # Comparing attendance percentage value with min_attendance_Required

        if attendance_calc_formula(present_slot, total_slot) == min_attendance_required:
            op2.write(f"You Require {required_slots} Slots more to reach 75% attendance <br> Then Your attendance will be: {attendance_calc_formula(present_slot, total_slot)} %")
            required_slots = 0          # for again starting the counter from 0
            break
        elif attendance_calc_formula(present_slot - 1, total_slot - 1) > min_attendance_required:
            op2.write(f"Chill! You are NOT in Detention List:), You already Have Sufficient Attendance\n")

            # to tell user, how much more bunk he/she can do...

            updated_present_slot = present_slot - 1  # 14 - 1 = 13 (original_present_slot)
            updated_total_slot = total_slot - 1  # 15 - 1 = 14 (original_total_slot)
            updated_required_slot = 0

            while True:
                updated_total_slot = updated_total_slot + 1  # 15, 16, 17, 18
                updated_required_slot = updated_required_slot + 1  # 1, 2, 3, 4
                attendance_calc_formula(updated_present_slot, updated_total_slot)

                # (13,14)->0->92.85, (13,15)->1->86.67, (13,16)->2->81.25, (13,17)->3->76.47, (13,18)->4->72.22

                if attendance_calc_formula(updated_present_slot, updated_total_slot) <= min_attendance_required:
                    op2.write(f"You can Bunk {updated_required_slot - 1} lectures <br> Your Attendance then will be {round(attendance_calc_formula(updated_present_slot, updated_total_slot - 1), 3)} % <br> Then after you can fall under Detention List")
                    break
            break
        else:
            continue

#-----------------------------------------------OVER---------------------------------------
