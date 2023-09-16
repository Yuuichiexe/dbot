import os
from pyrogram import Client, filters, idle
from PIL import Image, ImageDraw, ImageOps, ImageFont
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Madara import pgram as app

# Function to create a bold font
def get_bold_font(size):
    return ImageFont.truetype("Madara/resources/Vampire_Wars.ttf", size)

@app.on_message(filters.new_chat_members & filters.group)
async def welcome(_, message):
    for user in message.new_chat_members:
        try:
            profile_pic_url = user.photo.big_file_id
            response = await app.download_media(profile_pic_url)
            
            # Modify the dimensions and appearance of the welcome image as desired
            image_width = 1280
            image_height = 720
            
            # Load the custom welcome template image
            welcome_image = Image.open("Madara/resources/Untitled5_20230808001129.png")
            welcome_image = welcome_image.resize((image_width, image_height))
            
            # Load and resize the new user's profile picture
            profile_pic = Image.open(response)
            profile_pic_size = (350, 350)
            profile_pic.thumbnail(profile_pic_size)
            
            # Create a new blank image for the combined welcome image
            welcome_with_profile_pic = Image.new("RGB", (image_width, image_height), (0, 0, 0))
            
            # Calculate the position of the profile picture in the center of the welcome image
            profile_pic_position = ((image_width - profile_pic.size[0]) // 2, (image_height - profile_pic.size[1]) // 2)
            
            # Paste the welcome template onto the new image
            welcome_with_profile_pic.paste(welcome_image, (0, 0))
            
            # Draw the group name at the top with capital letters
            group_name = message.chat.title.upper()
            draw = ImageDraw.Draw(welcome_with_profile_pic)
            group_name_font = get_bold_font(50)
            group_name_width, group_name_height = draw.textsize(group_name, font=group_name_font)
            group_name_position = ((image_width - group_name_width) // 2, 50)
            draw.text(group_name_position, group_name, fill="black", font=group_name_font)
            
            # Draw the username on the welcome image
            draw = ImageDraw.Draw(welcome_with_profile_pic)
            font_size = 35
            font = ImageFont.truetype("Madara/resources/Big Space.otf", font_size)
            username_text = f"Name: {user.first_name}!"
            text_width, text_height = draw.textsize(username_text, font=font)
            text_position = ((image_width - text_width) // 2, profile_pic_position[1] + profile_pic_size[1] + 20)
            draw.text(text_position, username_text, fill="black", font=font)
            
            # Create a circular mask for the profile picture
            mask = Image.new("L", profile_pic.size, 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse((0, 0, profile_pic.size[0], profile_pic.size[1]), fill=255)
            profile_pic.putalpha(mask)
            
            # Add an outline to the profile picture
            outline_color = (255, 255, 255)  # White color for the outline
            border_width = 9  # Adjust the border width as desired
            profile_pic_with_outline = ImageOps.expand(profile_pic, border=border_width, fill=outline_color)            
            
            # Paste the circular profile picture onto the welcome image
            welcome_with_profile_pic.paste(profile_pic.convert("RGB"), profile_pic_position, profile_pic) 
            
            # Save the final welcome image with a unique name based on the user's ID
            welcome_image_path = f"welcome_{user.id}.jpg"
            welcome_with_profile_pic.save(welcome_image_path)
            
            # Specify the welcome message
            msg = f"""
**Hey! {user.mention}**, Welcome to {message.chat.title}! 🎉🎊
"""
            
            # Reply to the message with the custom welcome image and caption
            await message.reply_photo(photo=welcome_image_path, caption=msg)
            
            # Remove the temporary welcome image file
            welcome_with_profile_pic.close()
            os.remove(welcome_image_path)
        except Exception as e:
            print(f"Error sending welcome message for {user.first_name}: {str(e)}")

@app.on_message(filters.left_chat_member & filters.group)
async def goodbye(_, message):
    user = message.left_chat_member
    try:
        # Modify the dimensions and appearance of the goodbye image as desired
        image_width = 1280
        image_height = 720
        
        # Load the custom goodbye template image
        goodbye_image = Image.open("Madara/resources/Untitled5_20230808001129.png")
        goodbye_image = goodbye_image.resize((image_width, image_height))
        
        # Create a new blank image for the combined goodbye image
        goodbye_with_user = Image.new("RGB", (image_width, image_height), (0, 0, 0))
        
        # Calculate the position of the user's profile picture in the center of the goodbye image
        profile_pic_size = (350, 350)
        profile_pic_position = ((image_width - profile_pic_size[0]) // 2, (image_height - profile_pic_size[1]) // 2)
        
        # Draw the group name at the top with capital letters
        group_name = message.chat.title.upper()
        draw = ImageDraw.Draw(goodbye_image)
        group_name_font = get_bold_font(50)
        group_name_width, group_name_height = draw.textsize(group_name, font=group_name_font)
        group_name_position = ((image_width - group_name_width) // 2, 50)
        draw.text(group_name_position, group_name, fill="black", font=group_name_font)
       
        # Load and resize the user's profile picture
        profile_pic_url = user.photo.big_file_id
        response = await app.download_media(profile_pic_url)
        profile_pic = Image.open(response)
        profile_pic.thumbnail(profile_pic_size)
        
        # Paste the goodbye template onto the new image
        goodbye_with_user.paste(goodbye_image, (0, 0))
        
        # Draw the username on the goodbye image
        draw = ImageDraw.Draw(goodbye_with_user)
        font_size = 35
        font = ImageFont.truetype("Madara/resources/Big Space.otf", font_size)
        username_text = f"Goodbye, {user.first_name}!"
        text_width, text_height = draw.textsize(username_text, font=font)
        text_position = ((image_width - text_width) // 2, profile_pic_position[1] + profile_pic_size[1] + 20)
        draw.text(text_position, username_text, fill="black", font=font)
        
        # Create a circular mask for the profile picture
        mask = Image.new("L", profile_pic.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, profile_pic.size[0], profile_pic.size[1]), fill=255)
        profile_pic.putalpha(mask)
        
        # Paste the circular profile picture onto the goodbye image
        goodbye_with_user.paste(profile_pic.convert("RGB"), profile_pic_position, profile_pic) 
        
        # Save the final goodbye image with a unique name based on the user's ID
        goodbye_image_path = f"goodbye_{user.id}.jpg"
        goodbye_with_user.save(goodbye_image_path)
        
        # Specify the goodbye message caption
        caption = f"Goodbye, {user.first_name}! We'll miss you. 👋"
        
        # Send the goodbye image as a reply to the message with the caption
        await message.reply_photo(photo=goodbye_image_path, caption=caption)
        
        # Remove the temporary goodbye image file
        goodbye_with_user.close()
        os.remove(goodbye_image_path)
    except Exception as e:
        print(f"Error sending goodbye message for {user.first_name}: {str(e)}")
