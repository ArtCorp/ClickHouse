from testflows.core import *

from rbac.helper.common import *

@TestFeature
@Name("privileges")
def feature(self):

    tasks = []
    pool = Pool(16)

    try:
        try:
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.insert", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.select", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.show_tables", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.public_tables", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.distributed_table", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_column", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_index", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_constraint", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_ttl", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_settings", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_update", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_delete", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_freeze", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_fetch", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.alter.alter_move", "feature"), flags=TE), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.privileges.grant_option", "feature"), flags=TE), {})
        finally:
            join(tasks)
    finally:
        pool.close()
