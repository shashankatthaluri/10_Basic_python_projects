# Simple Python program for a console-based mini blog system

class MiniBlog:
    def __init__(self):
        self.posts = {}

    def create_post(self, title, content):
        self.posts[title] = content
        print("Blog post created successfully!")

    def display_posts(self):
        print("\nExisting Blog Posts:")
        for i, (title, content) in enumerate(self.posts.items(), 1):
            print(f"{i}. {title}\n   {content}\n")

    def edit_post(self, title, new_content):
        if title in self.posts:
            self.posts[title] = new_content
            print("Blog post edited successfully!")
        else:
            print("Blog post not found.")

    def delete_post(self, title):
        if title in self.posts:
            del self.posts[title]
            print("Blog post deleted successfully!")
        else:
            print("Blog post not found.")

def main():
    print("Welcome to Mini Blog System!")

    mini_blog = MiniBlog()

    while True:
        print("\n1. Create a new blog post")
        print("2. Display existing blog posts")
        print("3. Edit a blog post")
        print("4. Delete a blog post")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            title = input("Enter the title of the new blog post: ")
            content = input("Enter the content of the new blog post:\n")
            mini_blog.create_post(title, content)

        elif choice == '2':
            mini_blog.display_posts()

        elif choice == '3':
            title = input("Enter the title of the blog post to edit: ")
            new_content = input("Enter the new content of the blog post:\n")
            mini_blog.edit_post(title, new_content)

        elif choice == '4':
            title = input("Enter the title of the blog post to delete: ")
            mini_blog.delete_post(title)

        elif choice == '5':
            print("\nExiting Mini Blog System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()
