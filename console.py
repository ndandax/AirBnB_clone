#!/usr/bin/python3
"""command line interpreter"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
import re


class HBNBCommand(cmd.Cmd):
    """class for command line interpreter"""

    prompt = '(hbnb) '
    classList = ["BaseModel",
                 "User",
                 "Place",
                 "City",
                 "State",
                 "Amenity",
                 "Review"
                 ]

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def do_EOF(self, line):
        """End of File"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, instance):
        """creates new instance of basemodel"""
        args = instance.split()
        if len(args) == 0:
            print("** class name missing **")
        if args:
            try:
                if args[0] not in HBNBCommand.classList:
                    print("** class doesn't exist **")
                else:
                    new_instance = eval(args[0])()
                    new_instance.save()
                    print(new_instance.id)
            except Exception:
                pass


    def do_show(self, arg):
        """It Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classList:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """It Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classList:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """It prints : Prints all string representation of
        all instances based or not on the class name"""
        # args = arg.split()
        # objs = storage.all()
        # if len(args) > 0 and args[0] not in HBNBCommand.classList:
        #     print("** class doesn't exist **")
        # else:
        #     print([str(objs[obj]) for obj in objs])

        args = arg.split()
        objs = storage.all()
        if args:
            try:
                if args[0] not in HBNBCommand.classList:
                    print("** class doesn't exist **")
                else:
                    ss = [str(obj) for key, obj in storage.all().items()
                          if type(obj).__name__ == args[0]] 
                    print(ss)                   
            except Exception:
                pass
        else:
            ss = [str(obj) for key, obj in storage.all().items()]
            print(ss)

    def do_count(self, arg):
        """Counts the instances of a class.
        """
        args = arg.split()
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classList:
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    args[0] + '.')]
            print(len(matches))
        
    def do_update(self, arg):
        """it updates an instance based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classList:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] not in objects_dic:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0]+"."+args[1]
            attr = args[2]
            value = args[3].replace('"', ' ')
            inst = objects_dic[key]
            if hasattr(inst, attr) and type(getattr(inst, attr)) is int:
                if (value).isnumeric():
                    value = int(value)
            elif hasattr(inst, attr) and type(getattr(inst, attr)) is float:
                idk = args[3].split(".")
                if idk[0].isnumeric() and idk[1].isnumeric():
                    value = float(value)
            setattr(storage.all()[key], attr, value)
            storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
