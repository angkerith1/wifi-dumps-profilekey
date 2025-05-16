import subprocess
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from tkinter.font import Font
import webbrowser
from datetime import datetime
from PIL import Image, ImageTk

class WiFiProfileExtractorPro:
    def __init__(self, master):
        self.master = master
        self.bg_image = None
        self.bg_label = None
        self.setup_window()
        self.create_widgets()
        self.setup_styles()
        
    def setup_window(self):
        self.master.title("WiFi Profile Extractor Pro | DEV BY : @Rith")
        self.master.geometry("800x650")
        self.master.minsize(720, 580)
        
        # Set window icon (uncomment and provide path)
        # try:
        #     self.master.iconbitmap('your_icon.ico')
        # except:
        #     pass
        
        # Load background image
        try:
            bg_img = Image.open("background.png")  # Replace with your PNG path
            bg_img = bg_img.resize((800, 650), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(bg_img)
            self.bg_label = tk.Label(self.master, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Background image error: {e}")
            self.master.configure(bg="#2b3e50")  # Fallback color
        
        # Make window slightly transparent
        self.master.attributes('-alpha', 0.97)
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Custom styles with transparency
        self.style.configure('Main.TFrame', background='')
        self.style.configure('Header.TFrame', background='#2b3e50')
        self.style.configure('Footer.TFrame', background='#2b3e50')
        self.style.configure('Content.TFrame', background='#ffffff')
        
        # Transparent label styles
        self.style.configure('Title.TLabel', 
                           font=('Segoe UI', 16, 'bold'), 
                           foreground='white',
                           background='#2b3e50')
        self.style.configure('Subtitle.TLabel',
                           font=('Segoe UI', 9),
                           foreground='#bdc3c7',
                           background='#2b3e50')
        
        # Glass effect buttons
        self.style.configure('Accent.TButton',
                           font=('Segoe UI', 10, 'bold'),
                           foreground='white',
                           background='#3498db',
                           bordercolor='#3498db',
                           focuscolor='#3498db',
                           padding=10,
                           relief='flat')
        self.style.map('Accent.TButton',
                      background=[('active', '#2980b9')])
        
        self.style.configure('Secondary.TButton',
                           font=('Segoe UI', 9),
                           foreground='#7f8c8d',
                           background='#ecf0f1',
                           bordercolor='#bdc3c7',
                           padding=8)
        
    def create_widgets(self):
        # Main container with glass effect
        self.main_frame = ttk.Frame(self.master, style='Main.TFrame')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header with drop shadow effect
        self.header = ttk.Frame(self.main_frame, style='Header.TFrame', height=80)
        self.header.pack(fill='x')
        self.header.pack_propagate(0)
        
        self.title = ttk.Label(self.header, 
                             text="-> WiFi PROFILE EXTRACTOR\n-> DEV BY @RITHCYBER-TEAM", 
                             style='Title.TLabel')
        self.title.pack(side='left', padx=25, pady=10)
        
        self.subtitle = ttk.Label(self.header, 
                                text="Retrieve saved WiFi passwords | v1.1", 
                                style='Subtitle.TLabel')
        self.subtitle.pack(side='left', padx=10, pady=(0, 5))
        
        # Content area with glass effect
        self.content = ttk.Frame(self.main_frame, style='Content.TFrame')
        self.content.pack(fill='both', expand=True, pady=(0, 15))
        
        # Button panel with modern layout
        self.button_panel = ttk.Frame(self.content)
        self.button_panel.pack(fill='x', pady=(15, 10), padx=15)
        
        self.extract_btn = ttk.Button(self.button_panel, 
                                    text="🔍 EXTRACT PROFILES", 
                                    style='Accent.TButton',
                                    command=self.extract_profiles)
        self.extract_btn.pack(side='left', padx=(0, 10))
        
        self.export_btn = ttk.Button(self.button_panel,
                                   text="💾 EXPORT TO FILE",
                                   style='Secondary.TButton',
                                   command=self.export_to_file)
        self.export_btn.pack(side='left')
        
        # Modern output area with glass effect
        self.output_frame = ttk.Frame(self.content)
        self.output_frame.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        self.output_text = scrolledtext.ScrolledText(
            self.output_frame,
            font=('Consolas', 10),
            wrap=tk.WORD,
            padx=15,
            pady=15,
            bg='#ffffff',
            fg='#2c3e50',
            insertbackground='#3498db',
            selectbackground='#3498db',
            selectforeground='white',
            highlightthickness=1,
            highlightbackground='#bdc3c7',
            highlightcolor='#3498db',
            relief='flat',
            bd=0
        )
        self.output_text.pack(fill='both', expand=True)
        
        # Configure text tags with modern styling
        self.output_text.tag_configure('profile', foreground='#2c3e50', font=('Consolas', 10, 'bold'))
        self.output_text.tag_configure('password', foreground='#e74c3c', font=('Consolas', 10, 'bold'))
        self.output_text.tag_configure('header', foreground='#3498db', font=('Consolas', 12, 'bold'))
        self.output_text.tag_configure('success', foreground='#27ae60', font=('Consolas', 10))
        
        # Modern footer with copyright
        self.footer = ttk.Frame(self.main_frame, style='Footer.TFrame', height=45)
        self.footer.pack(fill='x')
        self.footer.pack_propagate(0)
        
        self.copyright = ttk.Label(
            self.footer,
            text=f"© {datetime.now().year} NDTSEC CYBER-GROUP. All Rights Reserved.",
            style='Subtitle.TLabel'
        )
        self.copyright.pack(side='left', padx=25)
        
        self.help_link = ttk.Label(
            self.footer,
            text="🆘 Help & Support",
            style='Subtitle.TLabel',
            cursor='hand2'
        )
        self.help_link.pack(side='right', padx=25)
        self.help_link.bind('<Button-1>', lambda e: webbrowser.open('https://t.me/angkerith_official'))
        
    def extract_profiles(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "⚡ Extracting WiFi profiles...\n\n", 'header')
        self.master.update()
        
        try:
            # Get all WiFi profiles
            profiles_data = subprocess.check_output('netsh wlan show profiles', shell=True, text=True)
            profiles = [line.split(":")[1].strip() 
                       for line in profiles_data.split('\n') 
                       if "All User Profile" in line]

            if not profiles:
                self.output_text.insert(tk.END, "❌ No WiFi profiles found on this system.\n", 'header')
                return

            self.output_text.insert(tk.END, f"✅ Found {len(profiles)} WiFi profiles:\n\n", 'header')
            
            # Process each profile
            for i, profile in enumerate(profiles, 1):
                self.output_text.insert(tk.END, f"🔹 Profile {i}: ", 'profile')
                self.output_text.insert(tk.END, f"{profile}\n")
                
                try:
                    # Get profile details
                    profile_info = subprocess.check_output(
                        f'netsh wlan show profile name="{profile}" key=clear', 
                        shell=True, 
                        text=True
                    )
                    
                    # Extract password if available
                    password = next((line.split(":")[1].strip() 
                                   for line in profile_info.split('\n') 
                                   if "Key Content" in line), None)
                    
                    self.output_text.insert(tk.END, "🔑 Password: ")
                    self.output_text.insert(tk.END, password if password else "[Not available]", 'password')
                    self.output_text.insert(tk.END, "\n\n")
                    
                except subprocess.CalledProcessError:
                    self.output_text.insert(tk.END, "⚠️ Error retrieving password (admin rights needed)\n\n")
                    
            self.output_text.insert(tk.END, "✔️ Extraction complete.\n", 'success')
            
        except subprocess.CalledProcessError:
            messagebox.showerror(
                "Admin Rights Required",
                "This operation requires Administrator privileges.\n\n"
                "Please right-click and select 'Run as Administrator'.",
                parent=self.master
            )
        except Exception as e:
            messagebox.showerror(
                "Unexpected Error",
                f"An error occurred: {str(e)}",
                parent=self.master
            )
            
    def export_to_file(self):
        content = self.output_text.get(1.0, tk.END)
        if not content.strip():
            messagebox.showwarning("Empty Content", "No data to export.", parent=self.master)
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save WiFi Profiles As",
            initialfile=f"wifi_profiles_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"╔{'═'*78}╗\n")
                    f.write(f"║ {'WiFi Profile Export':^76} ║\n")
                    f.write(f"║ {'-'*76} ║\n")
                    f.write(f"║ {'Date:':<10}{datetime.now().strftime('%Y-%m-%d %H:%M:%S'):>66} ║\n")
                    f.write(f"╚{'═'*78}╝\n\n")
                    f.write(content)
                messagebox.showinfo(
                    "Export Successful", 
                    f"Profiles successfully exported to:\n{file_path}", 
                    parent=self.master
                )
            except Exception as e:
                messagebox.showerror(
                    "Export Failed", 
                    f"Error saving file:\n{str(e)}", 
                    parent=self.master
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = WiFiProfileExtractorPro(root)
    root.mainloop()