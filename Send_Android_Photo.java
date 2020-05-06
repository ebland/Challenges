import io.appium.java_client.android.AndroidDriver;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;



public class Send_Android_Photo {
private static String ANDROID_PHOTO_PATH = "/mnt/sdcard/Pictures";
private static By backupSwitch = By.id("com.google.android.apps.photos:id/auto_backup_switch");
private static By touchOutside = By.id("com.google.android.apps.photos:id/touch_outside");
private static By keepOff = By.xpath("//*[@text='KEEP OFF']");
private static By photo = By.xpath("//android.view.ViewGroup[contains(@content-desc, 'Photo taken')]");
private static By trash = By.id("com.google.android.apps.photos:id/trash");
private static By moveToTrash = By.xpath("//*[@text='MOVE TO TRASH']");

@Test
public void testSeedPhotoPicker() throws IOException {
DesiredCapabilities capabilities = new DesiredCapabilities();
File classpathRoot = new File(System.getProperty("user.dir"));
capabilities.setCapability("platformName", "Android");
capabilities.setCapability("deviceName", "Android Emulator");
capabilities.setCapability("automationName", "UiAutomator2");
capabilities.setCapability("appPackage", "com.google.android.apps.photos");
capabilities.setCapability("appActivity", ".home.HomeActivity");

// Open the app.
AndroidDriver driver = new AndroidDriver<>(new URL("http://localhost:4723/wd/hub"), capabilities);
try {
// Check for existing photos
setupAppState(driver);
// Set up image to push to Google photos
File assetDir = new File(classpathRoot, "/Users/elizabethbland/Desktop/");
File img = new File(assetDir.getCanonicalPath(), "image_appium_challenge.jpg");
// Push the file
driver.pushFile(ANDROID_PHOTO_PATH + "/" + img.getName(), img);
// wait for image to upload in Google Photos Album, verify with WebDriverWait
WebDriverWait wait = new WebDriverWait(driver, 10);

ExpectedCondition condition = ExpectedConditions.numberOfElementsToBe(photo,1);
wait.until(condition);
} finally {
driver.quit();
}
}

public void setupAppState(AndroidDriver driver) {
// Get through the notifications, etc.
WebDriverWait wait = new WebDriverWait(driver, 10);
WebDriverWait shortWait = new WebDriverWait(driver, 3);
wait.until(ExpectedConditions.presenceOfElementLocated(backupSwitch)).click();
wait.until(ExpectedConditions.presenceOfElementLocated(touchOutside)).click();
wait.until(ExpectedConditions.presenceOfElementLocated(keepOff)).click();
//delete all existing pictures
try {
while (true) {
shortWait.until(ExpectedConditions.presenceOfElementLocated(photo)).click();
shortWait.until(ExpectedConditions.presenceOfElementLocated(trash)).click();
shortWait.until(ExpectedConditions.presenceOfElementLocated(moveToTrash)).click();
}
} catch (TimeoutException ignore) {}
}
