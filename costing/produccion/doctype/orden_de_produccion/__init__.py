import frappe

field_set_list = [
	{
		"station": "pre_station", 
		"hour_rate": "options_pre_hour_rate", 
		"status": "options_pre_status", 
		"operation": "pre_operation", 
		"in_qty": "pre_in_qty", 
		"out_qty": "pre_out_qty", 
		"real_start_time": "pre_real_start_time", 
		"real_end_time": "pre_real_end_time", 
		"real_time_in_minutes": "pre_real_time_in_minutes", 
		"real_total_cost": "options_pre_real_total_cost", 
	},
	{
		"station": "printer_station", 
		"hour_rate": "options_print_hour_rate", 
		"status": "options_print_status", 
		"operation": "print_operation", 
		"in_qty": "print_in_qty", 
		"out_qty": "print_out_qty", 
		"real_start_time": "print_real_start_time", 
		"real_end_time": "print_real_end_time", 
		"real_time_in_minutes": "print_real_time_in_minutes", 
		"real_total_cost": "options_print_real_total_cost", 
	},
	{
		"station": "cutter_station", 
		"hour_rate": "cutter_hour_rate", 
		"status": "cutter_status", 
		"operation": "cutter_operation", 
		"in_qty": "qty_into_paper_cutter", 
		"out_qty": "qty_out_paper_cutter", 
		"real_start_time": "cutter_real_start_time", 
		"real_end_time": "cutter_real_end_time", 
		"real_time_in_minutes": "cutter_real_time_in_minutes", 
		"real_total_cost": "cutter_real_total_cost", 
	},
	{
		"station": "options_control_station", 
		"hour_rate": "options_control_hour_rate", 
		"status": "options_control_status", 
		"operation": "options_control_operation", 
		"in_qty": "options_control_in_qty", 
		"out_qty": "options_control_out_qty", 
		"real_start_time": "options_control_real_start_time", 
		"real_end_time": "options_control_real_end_time", 
		"real_time_in_minutes": "options_control_real_time_in_minutes", 
		"real_total_cost": "options_control_real_total_cost", 
	},
	{
		"station": "options_protection_station_1", 
		"hour_rate": "options_protection_hour_rate_1", 
		"status": "options_protection_status_1", 
		"operation": "options_protection_operation_1", 
		"in_qty": "options_protection_in_qty_1", 
		"out_qty": "options_protection_out_qty_1", 
		"real_start_time": "options_protection_real_start_time_1", 
		"real_end_time": "options_protection_real_end_time_1", 
		"real_time_in_minutes": "options_protection_real_time_in_minutes_1", 
		"real_total_cost": "options_protection_real_total_cost_1", 
	},
	{
		"station": "options_protection_station_2", 
		"hour_rate": "options_protection_hour_rate_2", 
		"status": "options_protection_status_2", 
		"operation": "options_protection_operation_2", 
		"in_qty": "options_protection_in_qty_2", 
		"out_qty": "options_protection_out_qty_2", 
		"real_start_time": "options_protection_real_start_time_2", 
		"real_end_time": "options_protection_real_end_time_2", 
		"real_time_in_minutes": "options_protection_real_time_in_minutes_2", 
		"real_total_cost": "options_protection_real_total_cost_2", 
	},
	{
		"station": "options_cutter_station", 
		"hour_rate": "options_cutter_hour_rate", 
		"status": "options_cutter_status", 
		"operation": "options_cutter_operation", 
		"in_qty": "options_cutter_in_qty", 
		"out_qty": "options_cutter_out_qty", 
		"real_start_time": "options_cutter_real_start_time", 
		"real_end_time": "options_cutter_real_end_time", 
		"real_time_in_minutes": "options_cutter_real_time_in_minutes", 
		"real_total_cost": "options_cutter_real_total_cost", 
	},
	{
		"station": "options_union_station", 
		"hour_rate": "options_union_hour_rate", 
		"status": "options_union_status", 
		"operation": "options_union_operation", 
		"in_qty": "options_union_in_qty", 
		"out_qty": "options_union_out_qty", 
		"real_start_time": "options_union_real_start_time", 
		"real_end_time": "options_union_real_end_time", 
		"real_time_in_minutes": "options_union_real_time_in_minutes", 
		"real_total_cost": "options_union_real_total_cost", 
	},
	{
		"station": "options_folding_station", 
		"hour_rate": "options_folding_hour_rate", 
		"status": "options_folding_status", 
		"operation": "options_folding_operation", 
		"in_qty": "options_folding_in_qty", 
		"out_qty": "options_folding_out_qty", 
		"real_start_time": "options_folding_real_start_time", 
		"real_end_time": "options_folding_real_end_time", 
		"real_time_in_minutes": "options_folding_real_time_in_minutes", 
		"real_total_cost": "options_folding_real_total_cost", 
	},
	{
		"station": "options_utility_station_1", 
		"hour_rate": "options_utility_hour_rate_1", 
		"status": "options_utility_status_1", 
		"operation": "options_utility_operation_1", 
		"in_qty": "options_utility_in_qty_1", 
		"out_qty": "options_utility_out_qty_1", 
		"real_start_time": "options_utility_real_start_time_1", 
		"real_end_time": "options_utility_real_end_time_1", 
		"real_time_in_minutes": "options_utility_real_time_in_minutes_1", 
		"real_total_cost": "options_utility_real_total_cost_1", 
	},
	{
		"station": "options_utility_station_2", 
		"hour_rate": "options_utility_hour_rate_2", 
		"status": "options_utility_status_2", 
		"operation": "options_utility_operation_2", 
		"in_qty": "options_utility_in_qty_2", 
		"out_qty": "options_utility_out_qty_2", 
		"real_start_time": "options_utility_real_start_time_2", 
		"real_end_time": "options_utility_real_end_time_2", 
		"real_time_in_minutes": "options_utility_real_time_in_minutes_2", 
		"real_total_cost": "options_utility_real_total_cost_2", 
	},
	{
		"station": "options_utility_station_3", 
		"hour_rate": "options_utility_hour_rate_3", 
		"status": "options_utility_status_3", 
		"operation": "options_utility_operation_3", 
		"in_qty": "options_utility_in_qty_3", 
		"out_qty": "options_utility_out_qty_3", 
		"real_start_time": "options_utility_real_start_time_3", 
		"real_end_time": "options_utility_real_end_time_3", 
		"real_time_in_minutes": "options_utility_real_time_in_minutes_3", 
		"real_total_cost": "options_utility_real_total_cost_3", 
	},
	{
		"station": "options_texture_station_1", 
		"hour_rate": "options_texture_hour_rate_1", 
		"status": "options_texture_status_1", 
		"operation": "options_texture_operation_1", 
		"in_qty": "options_texture_in_qty_1", 
		"out_qty": "options_texture_out_qty_1", 
		"real_start_time": "options_texture_real_start_time_1", 
		"real_end_time": "options_texture_real_end_time_1", 
		"real_time_in_minutes": "options_texture_real_time_in_minutes_1", 
		"real_total_cost": "options_texture_real_total_cost_1", 
	},
	{
		"station": "options_texture_station_2", 
		"hour_rate": "options_texture_hour_rate_2", 
		"status": "options_texture_status_2", 
		"operation": "options_texture_operation_2", 
		"in_qty": "options_texture_in_qty_2", 
		"out_qty": "options_texture_out_qty_2", 
		"real_start_time": "options_texture_real_start_time_2", 
		"real_end_time": "options_texture_real_end_time_2", 
		"real_time_in_minutes": "options_texture_real_time_in_minutes_2", 
		"real_total_cost": "options_texture_real_total_cost_2", 
	},
	{
		"station": "options_packing_station", 
		"hour_rate": "options_packing_hour_rate", 
		"status": "options_packing_status", 
		"operation": "options_packing_operation", 
		"in_qty": "options_packing_in_qty", 
		"out_qty": "options_packing_out_qty", 
		"real_start_time": "options_packing_real_start_time", 
		"real_end_time": "options_packing_real_end_time", 
		"real_time_in_minutes": "options_packing_real_time_in_minutes", 
		"real_total_cost": "options_packing_real_total_cost", 
	}
]