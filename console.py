#!/usr/bin/python3
"""Command Line Interpreter"""
import cmd
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """CLI"""
    prompt = '(hbnb)'
    class_name = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def emptyline(self):
        """Do not execute the last command with an empty line"""
        pass

    def do_quit(self, line):
        """Quit the program"""
        raise SystemExit

    def do_EOF(self, line):
        """End of file"""
        print('')
        return True

    def do_create(self, line):
        """Create a new instance"""
        if not line:
            print("** class name missing **")
            return
        if line not in self.class_name:
            print("** class doesn't exist **")
            return

        new_obj = eval(line)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Show instance of a class with a specific id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on class and id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Print all instances or all instances of a specific class"""
        all_objs = storage.all()
        if not line:
            print([str(obj) for obj in all_objs.values()])
        elif line in self.class_name:
            print([str(obj) for obj in all_objs.values() if obj.__class__.__name__ == line])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Add or update an attribute for an instance"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        valid_types = ['my_number', 'number_rooms', 'number_bathrooms', 'max_guest', 'price_by_night']
        valid_types += ['latitude', 'longitude']

        if args[2] in valid_types:
            setattr(all_objs[key], args[2], int(args[3]) if args[2] in valid_types[:5] else float(args[3]))
            setattr(all_objs[key], 'updated_at', datetime.now())
            storage.save()
        else:
            setattr(all_objs[key], args[2], str(args[3]))
            setattr(all_objs[key], 'updated_at', datetime.now())
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

