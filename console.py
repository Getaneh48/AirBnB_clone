#!/usr/bin/python3
"""
a module that defines a command interpreter
"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A command interpreter class
    """

    prompt = '(hbnb) '
    models = ["BaseModel", "User", "State",
              "City", "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """
        Exits the command line
        Args:
            line(str): text
        """

        return True

    def do_EOF(self, line):
        """
        Exists the command line

        Args:
            line(str): text
        """

        return True

    def emptyline(self):
        """
        Prevents empty line and ENTER to be executed
        """
        pass

    def help_quit(self):
        """
        Help for the quit command
        """
        print("Quit command to exit the program")

    def is_class_method_format(self, line):
        """
        Checks if a given string is in the format
        '<classname>.<method>(args)'

        Args:
            line (str): string argument

        Returns:
            bool: True or False
        """

        pattern = r"^([A-Z][a-z0-9]*\.)?[a-z_][a-z0-9_]*\(([^)]*)\)$"

        return bool(re.match(pattern, line))

    def extract_method_info(self, text):
        """Extracts method name and arguments (if provided) from a string.

        Args:
            text (str): The string to extract information
                        from (format: "method(args)").

        Returns:
            tuple: A tuple containing the extracted
                   method name (or None if invalid)
                   and a list of arguments (or None if no arguments).
        """

        pattern = r"^([a-z_][a-z0-9_]*)\(([^)]*)\)$"
        match = re.match(pattern, text)
        if match:
            method_name = match.group(1)
            # Split arguments
            args = match.group(2).split(',')
            # Remove leading/trailing whitespaces
            args = [arg.strip().strip("'").strip('"') for arg in args]
            return method_name, args
        else:
            return None, None

    def precmd(self, line):
        if self.is_class_method_format(line):
            ls = line.split('.')
            className = ls[0]
            method, args = self.extract_method_info(ls[1])
            newline = f"{method} {className} {' '.join(args)}"
            print(newline)
            return newline

        return line

    def do_create(self, modelName):
        """
        Creates a new instance of a class, saves
        it (to the JSON file) and prints the id
        Ex: $ create BaseModel

        Args:
            modelName(str): class name of a model
        """

        if len(modelName) == 0:
            print("** class name missing **")
        elif modelName not in self.models:
            print("** class doesn't exist **")
        else:
            model = eval(f"{modelName}()")
            model.save()
            print(f"{model.id}")

    def help_create(self):
        """
        help for create command
        """

        print("Ex: create <class name>")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel

        Args:
            line(str): string containing list of args
        """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 0 and (args[0] not in self.models):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print('** no instance found **')
            else:
                print(objects[key])

    def help_show(self):
        """
        help for show command
        """

        print("Ex: show <class name> <id>")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        and saves the changes in to the JSON file

        Args:
            line(str): string containing arg lists
        """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 0 and (args[0] not in self.models):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print('** no instance found **')
            else:
                objects.pop(key)
                storage.save()

    def help_destroy(self):
        """
        help for destory command
        """

        print("Ex: destroy <class name> <id>")

    def do_all(self, modelName):
        """
        Prints all string representation of all
        instances based or not on the class name
        Ex: $ all BaseModel or $ all

        Args:
            modelName(str): the name of the model
        """

        if len(modelName) == 0:
            objects = storage.all()
            for key in objects.keys():
                print(objects[key])
        elif modelName not in self.models:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            for key in objects.keys():
                if key.startswith(modelName):
                    print(objects[key])

    def help_all(self):
        """
        help for the command all
        """
        print("Ex: all <class name> or all")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Args:
            line: string argument
        """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 0 and (args[0] not in self.models):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print('** no instance found **')
            else:
                obj = objects[key]
                if isinstance(args[2], str):
                    setattr(obj, args[2], str(args[3]))
                elif isinstance(args[2], int):
                    setattr(obj, args[2], int(args[3]))
                elif isinstance(args[2], float):
                    setattr(obj, args[2], float(args[3]))
                else:
                    pass
                storage.save()

    def help_update(self):
        """
        help for update command
        """

        print("Ex: update <class name> <id> <attrib> <value>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
