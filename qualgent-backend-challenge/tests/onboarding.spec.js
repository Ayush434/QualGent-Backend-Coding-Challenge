describe('Onboarding Tests', () => {
    it('should complete the onboarding process successfully', async () => {
        // Simulate user actions for onboarding
        await browser.url('https://example.com/onboarding');
        await $('#start-button').click();
        
        // Fill in onboarding form
        await $('#username').setValue('testuser');
        await $('#email').setValue('testuser@example.com');
        await $('#password').setValue('securepassword');
        await $('#submit-button').click();
        
        // Verify successful onboarding
        const successMessage = await $('#success-message').getText();
        expect(successMessage).toEqual('Onboarding completed successfully!');
    });

    it('should show an error for invalid email', async () => {
        // Simulate user actions for onboarding with invalid email
        await browser.url('https://example.com/onboarding');
        await $('#start-button').click();
        
        // Fill in onboarding form with invalid email
        await $('#username').setValue('testuser');
        await $('#email').setValue('invalid-email');
        await $('#password').setValue('securepassword');
        await $('#submit-button').click();
        
        // Verify error message
        const errorMessage = await $('#error-message').getText();
        expect(errorMessage).toEqual('Please enter a valid email address.');
    });
});