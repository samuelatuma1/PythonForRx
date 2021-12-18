estimated_oil_price = 54
available_expense = 1250000
wells = [
    {'name': 'OML-59-1', 'drill_cost': 390000, 'maintenance_cost': 100000, 'estimated_bbl_per_day': 500, 'total_days_active': 365 * 15},
    {'name': 'OML-59-2', 'drill_cost': 620000, 'maintenance_cost': 140000, 'estimated_bbl_per_day': 531, 'total_days_active': 365 * 15},
    {'name': 'OML-59-3', 'drill_cost': 420000, 'maintenance_cost': 80000, 'estimated_bbl_per_day': 451, 'total_days_active': 365 * 14},
    {'name': 'OML-59-4', 'drill_cost': 730000, 'maintenance_cost': 128000, 'estimated_bbl_per_day': 511, 'total_days_active': 365 * 15.5},
    {'name': 'OML-59-5', 'drill_cost': 350000, 'maintenance_cost': 90000, 'estimated_bbl_per_day': 411, 'total_days_active': 365 * 15},
    {'name': 'OML-59-6', 'drill_cost': 420060, 'maintenance_cost': 90000, 'estimated_bbl_per_day': 506, 'total_days_active': 365 * 15},
    {'name': 'OML-59-1', 'drill_cost': 391000, 'maintenance_cost': 120000, 'estimated_bbl_per_day': 506, 'total_days_active': 365 * 15},
    {'name': 'OML-59-2', 'drill_cost': 628000, 'maintenance_cost': 105000, 'estimated_bbl_per_day': 530, 'total_days_active': 365 * 14.992}
]



def find_best(wella, wellb):
    total_benefita = 0
    total_costa = 0
    for well in wella:
        total_benefita += (well['estimated_bbl_per_day'] * well['total_days_active'] * estimated_oil_price)
        total_costa += (well["drill_cost"]) + well["maintenance_cost"]
    
    total_benefitb = 0
    total_costb = 0
    for well in wellb:
        total_benefitb += (well['estimated_bbl_per_day'] * well['total_days_active'] * estimated_oil_price)
        total_costb += (well["drill_cost"]) + well["maintenance_cost"]
    
    return wella if (total_benefita - total_costa) >= (total_benefitb - total_costb) else wellb

well_options = {}
def optimize_available(wells, available_expense, curr_pos=0, choices=[]):
    if curr_pos in well_options.keys():
    
        return well_options[curr_pos]
    
    if available_expense <= 0 or curr_pos >= len(wells):
        return choices
    
    if (wells[curr_pos]['drill_cost'] + wells[curr_pos]['maintenance_cost'] ) > available_expense:
        
        return optimize_available(wells, available_expense, curr_pos=curr_pos + 1, choices=choices)
    else:
        well = wells[curr_pos]
        
        clone_choice = choices[:]
        
        clone_choice.append(well)
        invest_in_well = optimize_available(wells, available_expense-(well['drill_cost'] + well['maintenance_cost']), curr_pos=curr_pos + 1, choices=clone_choice)
        
        dont_invest = optimize_available(wells, available_expense, curr_pos=curr_pos + 1, choices=choices)
        
        
        decision = find_best(invest_in_well, dont_invest)
        well_options[curr_pos] = decision
        return decision
    
x = optimize_available(wells, available_expense)
print(x)
    

        