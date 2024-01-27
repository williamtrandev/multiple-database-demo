#
# class StaffRouter:
#     route_app_labels = {"staff"}
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return "staff_db"
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return "staff_db"
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#                 obj1._meta.app_label in self.route_app_labels
#                 or obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == "staff_db"
#         return None
#
#
# class CustomerRouter:
#     route_app_labels = {"customer"}
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return "customer_db"
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return "customer_db"
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#                 obj1._meta.app_label in self.route_app_labels
#                 or obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == "customer_db"
#         return None


class MultiDBRouter:
    route_app_labels = {"staff": "staff_db", "customer": "customer_db"}

    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        return self.route_app_labels.get(app_label, None)

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        return self.route_app_labels.get(app_label, None)

    def allow_relation(self, obj1, obj2, **hints):
        app_label1, app_label2 = obj1._meta.app_label, obj2._meta.app_label
        return app_label1 in self.route_app_labels or app_label2 in self.route_app_labels

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == self.route_app_labels.get(app_label, None)