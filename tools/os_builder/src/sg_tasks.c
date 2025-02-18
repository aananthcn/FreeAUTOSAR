#include <stddef.h>
#include <stdbool.h>
#include "sg_tasks.h"
#include "sg_appmodes.h"
#include "sg_events.h"
#include "sg_messages.h"
#include "sg_resources.h"


/*   T A S K   D E F I N I T I O N S   */
const OsTaskType _OsTaskList[] = {
	{
		.handler = OS_TASK(Task_A),
		.id = 0,
		.sch_type = NON_PREEMPTIVE,
		.priority = 1,
		.activations = 2,
		.autostart = true,
		.appmodes = (const AppModeType **) &Task_A_AppModes,
		.n_appmodes = TASK_A_APPMODE_MAX,
		.evtmsks = NULL,
		.n_evtmsks = TASK_A_EVENT_MAX,
		.msglist = NULL,
		.n_msglist = TASK_A_MESSAGE_MAX,
		.stack_size = 512
	},
	{
		.handler = OS_TASK(Task_B),
		.id = 1,
		.sch_type = NON_PREEMPTIVE,
		.priority = 2,
		.activations = 1,
		.autostart = false,
		.appmodes = NULL,
		.n_appmodes = TASK_B_APPMODE_MAX,
		.evtmsks = (const EventMaskType**) &Task_B_EventMasks,
		.n_evtmsks = TASK_B_EVENT_MAX,
		.msglist = NULL,
		.n_msglist = TASK_B_MESSAGE_MAX,
		.stack_size = 512
	},
	{
		.handler = OS_TASK(Task_C),
		.id = 2,
		.sch_type = NON_PREEMPTIVE,
		.priority = 3,
		.activations = 1,
		.autostart = true,
		.appmodes = (const AppModeType **) &Task_C_AppModes,
		.n_appmodes = TASK_C_APPMODE_MAX,
		.evtmsks = (const EventMaskType**) &Task_C_EventMasks,
		.n_evtmsks = TASK_C_EVENT_MAX,
		.msglist = NULL,
		.n_msglist = TASK_C_MESSAGE_MAX,
		.stack_size = 512
	},
	{
		.handler = OS_TASK(Task_D),
		.id = 3,
		.sch_type = NON_PREEMPTIVE,
		.priority = 4,
		.activations = 1,
		.autostart = false,
		.appmodes = NULL,
		.n_appmodes = TASK_D_APPMODE_MAX,
		.evtmsks = NULL,
		.n_evtmsks = TASK_D_EVENT_MAX,
		.msglist = NULL,
		.n_msglist = TASK_D_MESSAGE_MAX,
		.stack_size = 512
	},
	{
		.handler = OS_TASK(EcuM_StartupTwo),
		.id = 4,
		.sch_type = NON_PREEMPTIVE,
		.priority = 100,
		.activations = 1,
		.autostart = true,
		.appmodes = (const AppModeType **) &EcuM_StartupTwo_AppModes,
		.n_appmodes = ECUM_STARTUPTWO_APPMODE_MAX,
		.evtmsks = NULL,
		.n_evtmsks = ECUM_STARTUPTWO_EVENT_MAX,
		.msglist = NULL,
		.n_msglist = ECUM_STARTUPTWO_MESSAGE_MAX,
		.stack_size = 512
	},
	{
		.handler = OS_TASK(Ethernet_Tasks),
		.id = 5,
		.sch_type = NON_PREEMPTIVE,
		.priority = 10,
		.activations = 1,
		.autostart = true,
		.appmodes = (const AppModeType **) &Ethernet_Tasks_AppModes,
		.n_appmodes = ETHERNET_TASKS_APPMODE_MAX,
		.evtmsks = NULL,
		.n_evtmsks = ETHERNET_TASKS_EVENT_MAX,
		.msglist = NULL,
		.n_msglist = ETHERNET_TASKS_MESSAGE_MAX,
		.stack_size = 2048
	}
};


const u32 _OsTaskValidPriorities[] = {
	1, 2, 3, 4, 100, 10
};
